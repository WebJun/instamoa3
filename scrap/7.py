from Util import Util
import sys
import os
import aiohttp
import aiofiles
import asyncio
from urllib.parse import urlparse
import mimetypes
import traceback

urls = [
    'https://img.hankyung.com/photo/201412/01.9373989.1.jpg',
    'https://image.news1.kr/system/photos/2016/6/3/1964842/article.jpg',
    'https://img.hankyung.com/photo/201606/03.11780857.1.jpg',
    'https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/201603/24/htm_20160324192022724369.jpg',
    'https://news.imaeil.com/photos/2014/12/19/2014121914051443526_m.jpg',
    'http://img.newspim.com/content/image/2014/12/09/20141209000346_0.jpg',
    'https://dimg.donga.com/wps/SPORTS/IMAGE/2016/06/03/78490368.2.jpg',
    'https://dimg.donga.com/wps/NEWS/IMAGE/2015/09/26/68437954.6.jpg',
    'https://cdn.ppomppu.co.kr/zboard/data3/2022/0106/20220106104922_2C7xtO53Ql.jpg',
    'http://www.naewoeilbo.com/news/photo/202006/282796_72199_3559.png',
    'https://img.hankyung.com/photo/202205/BF.29907474.1.jpg',
    'https://blogthumb.pstatic.net/20141218_54/ceotip_1418907080254hUu5J_GIF/_0_%B9%CC%BE%B2%BF%A1%C0%CC_%BC%F6%C1%F6_%C6%D0%BC%C7.gif?type=w2',
    'http://menu.mtn.co.kr/upload/article/2014/12/09/2014120916074988690_00_249.jpg',
    'http://newsimg.wowtv.co.kr/20141209/B20141209142424900.jpg',
    'http://res.heraldm.com/content/image/2014/12/09/20141209001303_0.jpg',
    'https://image.edaily.co.kr/images/Photo/files/NP/S/2015/10/PS15101500737.jpg',
    'https://ilyo.co.kr/contents/article/images/2014/1214/1418563573820654.jpg',
    'https://file1.bobaedream.co.kr/multi_image/national/2017/02/09/19/CRc589c471a735bd.gif',
    'https://img3.daumcdn.net/thumb/R658x0.q70/?fname=http://t1.daumcdn.net/news/201603/24/ked/20160324093505067olbx.jpg',
    'https://img.sportsworldi.com/content/image/2014/12/09/20141209000976_0.jpg',
    'https://t1.daumcdn.net/cfile/tistory/2452244B5486D5420E',
    'https://img.hankyung.com/photo/201603/01.11447198.1.jpg',
    'https://www.koreapas.com/bbs/data/gofun/c83a32f76506aca5d16be155f5dab432.jpg',
    'https://thumb.zumst.com/530x0/https://static.news.zumst.com/images/91/2015/03/27/3d874f49308046ba891867ce9b4606d1.jpg',
    'http://img.tf.co.kr/article/home/2015/04/20/201590141429492378.jpg',
    'https://images.chosun.com/resizer/_pA2B0hjQ-cpGyU5uZaE9gQVsdo=/464x0/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/HMWGIA6E4L7QA4XIPUTXBPADYY.jpg',
    'https://cdn.stnsports.co.kr//news/photo/202204/148834_119374_5057.jpg',
    'https://wimg.mk.co.kr/meet/neds/2018/01/image_readtop_2018_72048_15173804943190992.jpg',
    'https://s.gae9.com/trend/2c9239d39e69e4b8.orig',
    'https://pickcon.co.kr/site/data/img_dir/2014/12/09/2014120903078_0.jpg',
    'https://edgio.clien.net/F01/2441083/9659e5f9051845dc890.GIF',
    'https://img.seoul.co.kr/img/upload/2014/12/09/SSI_20141209112211_V.jpg',
    'http://cdnimage.dailian.co.kr/news/201412/news_1418091398_474616_m_1.png',
    'https://m.segye.com/content/image/2012/11/30/20121130020004_0.jpg',
    'https://mblogthumb-phinf.pstatic.net/MjAyMDAxMjJfMjQ1/MDAxNTc5NjcxNDA5NDM3.oM9JOCHzJueN97o4vZ5DdeP-EjkpPNZuLY40mnyjUsog.Ucdfw6KkyEoyT1FQeVRPK8L_T1DK3mgYtFBFnGpt1jgg.JPEG.estattoo/227298_83196_3633.jpg?type=w800',
    'https://i.ytimg.com/vi/yfgNR-sMOWQ/hqdefault.jpg',
    'https://www.stnsports.co.kr/news/photo/201901/85767_48022_1252.jpg',
    'https://cphoto.asiae.co.kr/listimglink/1/2017100422531292904_1.jpg',
    'https://thumbnews.nateimg.co.kr/view610///news.nateimg.co.kr/orgImg/hm/2021/10/22/202110220650444225101_20211022065106_01.jpg',
    'https://ncache.ilbe.com/files/attach/new/20140120/4255758/1744343304/2789455891/bfae7f3e5ee26e15e6edbcb441a44e4a.jpg',
    'https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/201312/02/htm_20131202133135c010c011.jpg',
    'https://image.xportsnews.com/contents/images/upload/article/2017/0718/1500350599466887.jpg',
    'https://images.chosun.com/resizer/QH-VPwHvLmGMWikzfjCIoNBmHds=/446x251/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/F5YGND5FWDCCSOQCUSTP3ZCFNQ.jpg',
    'https://i.ytimg.com/vi/GJDyZ9IGPTw/maxresdefault.jpg',
    'https://file.sportsseoul.com/news/legacy/wyzmob/images/20150329/20150329_1427606810_34811300_1.jpg',
    'https://image.news1.kr/system/photos/2018/11/28/3409616/article.jpg',
    'https://talkimg.imbc.com/TVianUpload/TVian/TViews/image/2015/09/03/spotv_26919_37600_5635.jpg',
    'https://mblogthumb-phinf.pstatic.net/MjAxNzAxMTZfMjM3/MDAxNDg0NTAwNTY2MzQ1.1sGK5HCAFHBUo0yptMAw3umx-C6jlPaJxJs0PWQjxJQg.MKqHZSgYKIkDvl5YI1nNWaDMthy7slW7PaOKJ0f69_8g.JPEG.azuresee/downloadfile-40.jpg?type=w800',
    'https://dimg.donga.com/a/450/0/95/5/wps/NEWS/IMAGE/2013/09/09/57552419.5.jpg',
    'http://db.kookje.co.kr/news2000/photo/2016/1116/L20161116.99002171803i1.jpg',
    'https://www.cstimes.com/news/photo/201502/169156_151702_160.jpg',
    'https://photo.newsen.com/news_photo/2012/09/18/201209180807320610_1.jpg',
    'https://image.edaily.co.kr/images/Photo/files/NP/S/2015/10/PS15101500735.jpg',
    'https://images.chosun.com/resizer/sidmNXT9VAgHNsCENfxE-edB67E=/450x759/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/JPC2N6YX2LKH2IDSRRLUDZOCDM.jpg',
    'http://photo.isportskorea.com/photo/images/2013/11/20131119211607209.jpg',
    'https://news.nateimg.co.kr/orgImg/is/2022/06/04/d706bea5-13e8-43c7-976e-1c1fb45962a6.jpg',
    'https://img.mbn.co.kr/filewww/news/other/2014/12/09/110301903005.jpg',
    'http://res.heraldm.com/content/image/2016/03/25/20160325001369_0.jpg',
    'https://4.bp.blogspot.com/-2mwThVYUIYA/Wg1qDeZO1SI/AAAAAAAGMLI/52bEA5yI7ZIJ7d6EqnbntyldajfYwhQegCLcBGAs/s1600/1.gif',
    'https://image.news1.kr/system/photos/2014/6/20/905636/article.jpg/dims/optimize',
    'https://thumbnews.nateimg.co.kr/view610///onimg.nate.com/orgImg/sp/2014/12/09/20141209_1418080398_42255800_1.jpg',
    'https://static.news.zumst.com/images/51/2017/06/15/cd6c5ced70e74fe4b5f3c1377e4b5e34.jpg',
    'https://spnimage.edaily.co.kr/images/Photo/files/NP/S/2013/07/PS13072900046.jpg',
    'https://images.chosun.com/resizer/ZxCKffCGo7jRkfrSE1RER-QDOAs=/464x0/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/YVDLHBYBUAUUXBHLMWO2RGNYDA.jpg',
    'http://cdnimage.dailian.co.kr/news/201703/news_1490343357_620855_m_1.jpg',
    'https://img.hankyung.com/photo/201605/03.11684298.1.jpg',
    'https://mblogthumb-phinf.pstatic.net/20120306_276/iphongs_1330997846276jUs6k_JPEG/2.jpg?type=w2',
    'https://images.chosun.com/resizer/fRk0Q7TblUE1KTxMZlWZZ-dV1Q4=/464x0/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/UVLWXW7IVYHRV62EH6WUQIT6VI.jpg',
    'http://menu.mtn.co.kr/upload/article/2014/12/09/2014120917460666958_00_699.jpg',
    'https://nimage.g-enews.com/phpwas/restmb_allidxmake.php?idx=5&simg=20150531145646605998701_20150531150021_01_genews.jpg',
    'https://www.bntnews.co.kr/data/bnt/image/201311/31bd83f305143b73158b1f8b9d16ca45.jpg',
    'https://cphoto.asiae.co.kr/listimglink/1/2014120910384374109_1.jpg',
    'http://www.tvdaily.co.kr/upimages/gisaimg/201611/1479284720_1181742.jpg',
    'http://www.obsnews.co.kr/news/photo/201412/855276_154394_5057.jpg',
    'https://cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/YMEBZ2FSQHT7TNYVTFHIUIIPGU.jpg',
    'http://img2.sbs.co.kr/img/seditor/VD/2017/07/17/VD31328621_w1279.jpg',
    'https://photo.jtbc.co.kr/news/2013/07/29/20130729093202782.jpg',
    'https://img.hankyung.com/photo/201510/03.10701516.1.jpg',
    'https://wimg.mk.co.kr/meet/neds/2020/01/image_readtop_2020_60023_15793395524056949.jpg',
    'https://dispatch.cdnser.be/wp-content/uploads/2016/06/20160604001945_ijn_0529.jpg',
    'http://thumbnail.egloos.net/460x0/http://pds27.egloos.com/pds/201302/21/78/d0176178_5124fd6c0c1e4.jpg',
    'https://file.sportsseoul.com/news/legacy/wyzmob/images/20150323/20150323_1427085934_23164300_1.jpg',
    'http://res.heraldm.com/phpwas/restmb_jhidxmake.php?idx=5&simg=202104091109398857591_20210409111304_01.jpg',
    'https://getfile.fmkorea.com/getfile.php?code=248dc22044967df9b2f4b86ee6e94d55&file=http%3A%2F%2Fwww.ilbe.com%2Ffiles%2Fattach%2Fimages%2F377678%2F709%2F338%2F095%2F31cef93b6ed005b266da8d8df5a63c19.JPG&',
    'https://image.kmib.co.kr/online_image/2015/0915/201509150003_61180009856233_1.jpg',
    'https://i2.tcafe2a.com/210131/1888925213_rCbt4uAn_35d8fcff2ee5f5fb798d3ba10acda7bf8cafa7d4.jpg',
    'https://news.imaeil.com/photos/2013/05/20/2013052016165178081_m.jpg',
    'http://img.sportsworldi.com/content/image/2014/07/24/20140724000261_0.jpg',
    'http://www.newsinside.kr/news/photo/201510/353361_136492_3725.jpg',
    'https://img.jjang0u.com/data3/chalkadak/306/201301/12/135795708624719.jpg',
    'https://img.sbs.co.kr/newsnet/etv/upload/2013/07/29/30000302882_500.jpg',
    'https://cdn.cctoday.co.kr/news/photo/201412/871936_280167_5637.jpg',
    'http://newsimg.wowtv.co.kr/20141106/B20141106092117993.jpg',
    'http://img.segye.com/content/image/2015/11/18/20151118002553_0.jpg',
    'https://sports.hankooki.com/news/photo/202102/img_6579070_0.jpg',
    'https://scsgozneamae10236445.cdn.ntruss.com/data2/content/image/2013/05/20/.cache/512/201305200221265.jpg',
    'https://cdn.polinews.co.kr/news/photo/201511/253250_1.jpg',
    'https://image.ajunews.com/content/image/2015/04/03/20150403182624407791.jpg',
    'https://file.thisisgame.com/upload/tboard/user/2013/05/07/20130507100318_8104.0101cf375187d74927b213',
    'https://img.etnews.com/news/article/2016/11/16/cms_temp_article_16231521302932.jpg',
]

# urls = ['https://img.etnews.com/news/article/2016/11/16/cms_temp_article_16231521302932.jpg']


def get_extension_from_mime_type(mime_type):
    extension = mimetypes.guess_extension(mime_type, strict=False)
    if extension:
        return extension[1:]
    else:
        return None


async def requestImgAsync(url):
    try:
        fpn = ''
        parsed_uri = urlparse(url)
        filename, ext = os.path.splitext(parsed_uri.path)
        filename = os.path.basename(filename)
        ext = ext.lower()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as res:
                if ext not in ['.jpg', '.jpeg', '.png', '.gif']:
                    mime_type = res.headers['Content-Type']
                    ext = '.' + get_extension_from_mime_type(mime_type)
                else:
                    pass
                fpn = f'appdata/test/{util.now()}_{filename}{ext}'
                async with aiofiles.open(fpn, 'wb') as f:
                    await f.write(await res.read())
    except aiohttp.client_exceptions.ClientConnectorError as e:
        print(url, 997)
    except aiohttp.client_exceptions.ClientConnectorCertificateError as e:
        print(url, 9971)
    except Exception as e:
        print(url, 9972)
        print(traceback.format_exc())

util = Util()
tasks = [requestImgAsync(url) for url in urls]
loop = asyncio.get_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(asyncio.wait(tasks))
'''
확장자
hedaer Content-Type
MIME타입
파일내용
'''
