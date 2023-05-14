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
    'https://files.premium.sbs.co.kr/thumbnail/2023/05/04/1683175371790ha0ux37ydtv.gif',
    'https://www.seoulfn.com/news/photo/202303/482095_244631_3214.gif',
    'https://www.seoulfn.com/news/photo/202011/402433_179420_519.gif',
    'http://m.dayroze.com/web/product/big/202207/cea52e8c52edd96e061dd3ff327eeddd.gif',
    'https://i.namu.wiki/i/-7qrXZXmnBp5pHtD4sV6w9Y_eo00rgeK1lCEIAJ_p-UuZ9iGB_1UmgSd-Ydu3ojRx7LmcBLGluMJWkoFWiYeAA.gif',
    'https://i.namu.wiki/i/jt0zEmwg-yfkOlgoTI5-NqRAplUuR9J55_FnMw_qzlHW0XKAHEzgZyrkajwe9-6pyZiX0w-DW0ZjHnzWhzCt6Q.gif',
    'https://www.mcst.go.kr/attachFiles/cultureInfoCourt/monthServ/1382595162323.gif',
    'https://menu.mt.co.kr/animated/mt/2021/07/2021072709570644840_animated_1039210.gif',
    'https://i.pinimg.com/originals/1a/76/50/1a7650b84679b684d09ebf96f8b35b2b.gif',
    'https://talkimg.imbc.com/TVianUpload/tvian/TViews/image/2023/04/17/365ccd9e-103f-40b3-a592-d0dfb37c07ed.gif',
    'https://cdn.todayflow.co.kr/news/photo/202305/1085_5389_027.gif',
    'https://www.seoulfn.com/news/photo/202105/418622_192849_5348.gif',
    'https://blogthumb.pstatic.net/MjAxNzEyMjdfMTUx/MDAxNTE0MzQwNTE2NTg0.JkSxZm3uRkSxgb3kWS1BYqM3ly16fJPE_qu9yuaCeiMg.tI_5yHusoB-JYf_hr2fGYXlXfwx9WkZXgSwVw6KEkkUg.GIF.twinkle_co/IMG_2899.GIF?type=w2',
    'https://i.pinimg.com/originals/6a/be/55/6abe5547a820f83b097f858bec57944a.gif',
    'https://media.tenor.com/2wUzXNHcZpQAAAAC/iu-%EC%95%84%EC%9D%B4%EC%9C%A0.gif',
    'https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/201705/01/802a01ba-8086-4463-92c0-752b88c48861.gif',
    'https://mblogthumb-phinf.pstatic.net/MjAyMjEwMTFfMjY0/MDAxNjY1NDkzMDY2ODEy.r2DUp41vNSGkjYkR72DGH7kRr4G8teLm7dG3C3QHj-Qg.wnN5WBVCbN7NPbB078bGiFgWQ0Smr-AYdjP6iavMmngg.GIF.rend_/%EC%A0%9C%EB%AA%A9-%EC%97%86%EC%9D%8C1.gif?type=w800',
    'https://media.tenor.com/UXfPzS7Dvw0AAAAd/iu-%EC%95%84%EC%9D%B4%EC%9C%A0.gif',
    'https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/201310/08/htm_20131008145436c040c011.gif',
    'https://blog.kakaocdn.net/dn/BvMgU/btrSI8Sod4s/hRTTH3kkC5D8mI7entiSL0/img.gif',
    'https://spnimage.edaily.co.kr/images/Photo/files/NP/S/2022/06/PS22061800019.gif',
    'http://images.hkn24.com/news/photo/201209/105465_92679_536.gif',
    'https://blog.kakaocdn.net/dn/mMihL/btr4jKlEETL/o33NqpBl62BJzp2DDOMpDk/img.gif',
    'https://i.namu.wiki/i/ReBsZMB2t4-U0b_yDhVi_KWBSPG--aZ0kLlXWmzuoJnZydPhQvcvPlzzOzJS6te1YPht4_kaeIIt4t8UFEmnPQ.gif',
    'https://i1.daumcdn.net/thumb/R800x0/?fname=https://blog.kakaocdn.net/dn/beuLH3/btq1R8Yo9dj/MYufk6Dwr2EEqA4KHKr97k/img.gif',
    'https://www.seoulfn.com/news/photo/202203/450309_218362_153.gif',
    'https://i.pinimg.com/originals/a1/ff/7c/a1ff7c2bfbd247627ba07108fbf1092e.gif',
    'http://www.ifamily.co.kr/image/icard/372134/5fec3d13d6bcc_3232256098.gif',
    'https://www.reportdown.co.kr/View/%EC%95%84%EC%9D%B4%EC%9C%A0%EB%A1%9C%20%EB%B3%B8%20%EB%A1%9C%EC%97%94%20%EC%97%94%ED%84%B0%ED%85%8C%EC%9D%B8%EB%A8%BC%ED%8A%B8%EC%9D%98%20%EB%A7%88%EC%BC%80%ED%8C%85_hwp_03.gif',
    'https://t1.daumcdn.net/news/201704/21/mbn/20170421172038887kvou.gif',
    'https://static.inews24.com/v1/c8b873c1d83f86.gif',
    'https://media.tenor.com/uyADsD5G6QAAAAAC/iu-upset.gif',
    'http://img.tf.co.kr/article/home/2020/03/06/202078371583476299.gif',
    'https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/201707/08/190d64af-0f50-455e-ae33-57453ac38d68.gif',
    'https://post-phinf.pstatic.net/MjAyMDAyMjhfNyAg/MDAxNTgyODc1MjE5OTI2.E17Bhe29zfHHo2cq3gxizQvG7vabgtS19-FKCLB6Zygg.i4UXMjzfL3D7xWdGRghvWCco0-8CFlHVSU9-VIqXQZ0g.GIF/ec8820408bcf838979006d65a9a8f279.gif?type=w1200',
    'http://images.hkn24.com/news/photo/201112/87575_76748_418.gif',
    'https://d2u3dcdbebyaiu.cloudfront.net/uploads/atch_img/509/c75cd507e86b088d672d6e4536614c55_res_a..gif',
    'http://img.tf.co.kr/article/home/2020/09/18/202073891600413756.gif',
    'http://www.consumernews.co.kr/news/photo/201103/83835_3888fb334d8365ff0434ac812ea65910.gif',
    'http://www.filetalk.net/data/editor/2110/c72b90559ecc0098498f4587a13b829e_1634275391_4255.gif',
    'https://gamewinds.co.kr/data/editor/2104/0fd46f82da471f47651eef543df58a87_1617429359_4438.gif',
    'https://i.namu.wiki/i/nT5pD0zQJxddivhzOBd5ituY_kLPahP8EeEtSbkME9-kkBCWr6slg5NYvA5ahbLmDCRYwyaOP9qdzPKy70yG1A.gif',
    'https://t1.daumcdn.net/news/202009/20/THEFACT/20200920000147062hpjf.gif',
    'https://cdn.gotitstyle.com/news/photo/202303/680_5097_1541.gif',
    'http://ugogirl113.img.hhosting.kr/SH20111024000001/JEALOUSY/_MV_%20IU(%EC%95%84%EC%9D%B4%EC%9C%A0)%20_%20strawberry%20moon_1280x72021-10-19-11-19-31.gif',
    'http://newsimg.hankookilbo.com/2015/08/26/201508261038023285_6.jpg',
    'https://talkimg.imbc.com/TVianUpload/tvian/TViews/image/2023/04/17/d0f7401b-6380-47bf-9586-23b417e6df7c.gif',
    'https://thumbs.gfycat.com/CompetentAggravatingGallowaycow-size_restricted.gif',
    'https://blog.kakaocdn.net/dn/IQjQ5/btrZV7NraFR/qdkrcUzeNkqyksepUBxjK1/img.gif',
    'https://musicscore.co.kr/singerimg/%EC%95%84%EC%9D%B4%EC%9C%A034.gif',
    'https://photo.coolenjoy.co.kr/data/editor/2211/36c7f68ae513e98eb7f08c524d979f24ccd17a60.gif',
    'https://iyouwear.com/web/product/big/202112/32583b5c2dffbd6842a47af2b76c90bb.gif',
    'https://img.seoul.co.kr/img/upload/2022/05/27/SSI_20220527134035.gif',
    'https://s3.orbi.kr/data/file/united/9898ed2cf085e63f3be94094d8a84673.gif',
    'https://flowersonyou.co.kr/web/product/big/202012/f97a60239dfb055eace68a7631a553e3.gif',
    'https://thumbs.gfycat.com/SafeLivelyGroundhog-size_restricted.gif',
    'https://www.seoulfn.com/news/photo/202105/419162_193291_110.gif',
    'https://ekwjd3928.diskn.com/shop/190111/09/re/190111_09_re_02.gif',
    'https://blogthumb.pstatic.net/MjAxNjEyMTFfMjA5/MDAxNDgxNDI2MjYzNTM5.Lpr1rh0mmv2yPz4gnvrUccW5N8YsWp4iLt_lLEIuGRMg.KS5DRZWVOyYfuyzRuz-OOVqXWbHYOiAqCshJFa2VG7Ug.GIF.chrismen/I-07.gif?type=w2',
    'https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/201706/12/97d5614c-10f3-4542-bb35-20e27806a980.gif',
    'https://static-storychat.pstatic.net/2321252_27094293/d42i9a2312k5050.gif?type=rsc5',
    'https://t1.daumcdn.net/cfile/tistory/99BF4142601363E909',
    'http://brandconti.com/wp-content/uploads/2020/04/2019.%EB%84%A4%EC%9D%B4%EC%B3%90%EC%9C%84%EB%93%9C-%EC%95%84%EC%9D%B4%EC%9C%A0%ED%8E%B8001.gif',
    'https://cdn.allets.com/old/data/file/STAR/6FYtJBECRWhKZwWDYFPh.gif',
    'https://upload3.inven.co.kr/upload/2023/04/06/bbs/i013525657640.gif',
    'https://menu.mt.co.kr/animated/mt/2022/12/2022121111130755271_animated_1150320.gif',
    'https://image.nbkorea.com/NBRB_Site/20230428/NB20230428082709093001.gif',
    'http://www.stardailynews.co.kr/news/photo/201812/226910_258592_2426.gif',
    'http://image.musinsa.com/mfile_s01/2011/11/30/2bb56616e8958eff4705df1c61b60c0f165550.gif',
    'http://www.hungryboarder.com/files/attach/images/66/540/875/046/861192d6e090ad03ba9f8ce932296db1.gif',
    'https://media.tenor.com/tKWrKw6-doEAAAAC/%EC%95%84%EC%9D%B4%EC%9C%A0-%EC%95%84%EC%9D%B4%EC%9C%A0%EC%9C%99%ED%81%AC.gif',
    'https://image.kmib.co.kr/online_image/2022/0528/2022052817125021415_1653725570_0017125642.gif',
    'https://webimg.jestina.co.kr/UpData2/item/G2000024607/20220510125554S.gif',
    'https://cdn.mule.co.kr/data/original/2023/03/08/0780ce40-bd62-11ed-80ae-7db06350da58.gif',
    'https://cdn.k-trendynews.com/news/photo/202210/148310_199890_2614.gif',
    'http://www.hkn24.com/news/photo/201011/59073_52242_2946.gif',
    'https://blog.kakaocdn.net/dn/b8Pb8s/btr9DHLX26r/KCrGd5m83Bstn163aidYxK/img.gif',
    'https://d2u3dcdbebyaiu.cloudfront.net/uploads/atch_img/51/f3bb49df9b33908c304a9bbb08ba63f0_res_a..gif',
    'http://www.musicscore.co.kr/singerimg/%EC%95%84%EC%9D%B4%EC%9C%A016.gif',
    'https://t1.daumcdn.net/news/202009/20/THEFACT/20200920000159057pedl.gif',
    'http://www.mediaus.co.kr/news/photo/201609/66473_135110_217.gif',
    'https://i.pinimg.com/originals/81/ae/b0/81aeb0aea55f640287911a79b6d572b0.gif',
    'https://file.thisisgame.com/upload/tboard/user/2014/02/07/20140207170112_8977.gif',
    'https://www.seoulfn.com/news/photo/202103/412133_187398_216.gif',
    'https://cdn.mule.co.kr/data/original/2023/03/08/01c9f210-bd62-11ed-80ae-7db06350da58.gif',
    'http://www.stardailynews.co.kr/news/photo/201803/188279_222170_3419.gif',
    'http://image.musinsa.com/mfile_s01/2011/11/30/cc11b17d85935546ff483214d438bd70165619.gif',
    'http://img2.sbs.co.kr/img/sbs_cms/VD/2019/09/02/VD48456600_w640_h360.gif',
    'https://pds.joongang.co.kr//news/component/htmlphoto_mmdata/201710/10/42c06c8d-0ca5-441e-a8cf-49f2874063ba.gif',
    'https://i.namu.wiki/i/NrQBcu4_Tvvq0rcCW45nrHoqi1cuZeDTfd0dsMJnk_Dkq34XEuDYJ7JfxQSy6fze7nfAChPk_6Rlo8UdtBxgsw.gif',
    'https://timecker.com/files/attach/images/72164/755/074/99aee7d059443aab1e625d2c1c84ab6d.gif',
    'http://cdn.ggilbo.com/news/photo/202212/949848_783317_1153.gif',
    'https://onimg.nate.com/orgImg/ma/2016/08/31/65122_134459_3514.gif',
    'https://webimg.jestina.co.kr/UpData2/item/G2000025815/20221118114840M.gif',
    'https://coolenjoy.net/data/editor/2101/f9beead3057aaf76bc972f29ef087867718b3278.gif',
    'https://upload3.inven.co.kr/upload/2023/04/12/bbs/i016154776547.gif',
    'http://img.tf.co.kr/article/home/2016/08/27/20166534147230013802.gif',
    'https://media.tenor.com/4O9U_FD3v4cAAAAC/iu-%EC%95%84%EC%9D%B4%EC%9C%A0.gif',
    'https://newsimg.sedaily.com/2021/04/09/22L0NILFNL_20.gif',
    'https://mblogthumb-phinf.pstatic.net/MjAyMTA5MTdfMTkx/MDAxNjMxODY3MzM5NDk3.oi9WNwos36HTOsWjHVpevAFFyzPCQwoX75H5fDKhM3Yg.Q5DOW6do4dRKgqbSUeyQHXv-AjIbWXXLujjqG-ROlvcg.GIF.dltpdud03/img%EF%BC%8D112_%EF%BC%881%EF%BC%89.gif?type=w800',
]


async def requestImgAsync(uri):
    parsed_uri = urlparse(uri)
    filename, _ = os.path.splitext(parsed_uri.path)
    filename = os.path.basename(filename)
    fpn = f'appdata/test/{filename}.gif'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(uri) as res:
                async with aiofiles.open(fpn, 'wb') as f:
                    await f.write(await res.read())
    except Exception as e:
        print(uri, 9972)
        print(traceback.format_exc())

if __name__ == '__main__':
    tasks = [requestImgAsync(url) for url in urls]
    loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(asyncio.wait(tasks))
