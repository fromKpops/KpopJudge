import random

HYBE_qoo10_url=['https://www.qoo10.jp/su/1410613255/Q189976361',
          'https://www.qoo10.jp/su/1410613787/Q189976361',
          'https://www.qoo10.jp/su/1410614705/Q189976361']
HYBE_amz_url=['https://amzn.to/49ZTmBp',
          'https://www.amazon.co.jp/dp/B0BL7HWST7/ref=cm_sw_r_as_gl_api_gl_i_KH0N7RYBY04RY3WWEDZA?linkCode=ml2&tag=fromkpopsto-22',
          'https://amzn.to/4bWHqlB']
HYBE_img=['https://gd.image-qoo10.jp/li/261/657/4486657261.g_400-w-st_g.jpg',
          'https://gd.image-qoo10.jp/li/741/855/5445855741.g_400-w-st_g.jpg',
          'https://gd.image-qoo10.jp/li/341/660/5520660341.g_400-w-st_g.jpg']
HYBE_qoo10_intro=['【BTS】ジョングク愛用アイテム',
            '【LE SSERAFIM】サクラpickアイテム',
            '【LE SSERAFIM】チェウォンpickアイテム']
HYBE_amz_intro=['【BTS】ジョングク愛用アイテム',
            '【LE SSERAFIM】サクラpickアイテム',
            '【LE SSERAFIM】チェウォンpickアイテム']

JYP_qoo10_url=['https://www.qoo10.jp/su/1410617016/Q189976361',
         'https://www.qoo10.jp/su/1410616105/Q189976361',
         'https://www.qoo10.jp/su/1410617568/Q189976361']
JYP_amz_url=['https://amzn.to/48CBL1i',
         'https://amzn.to/3P4SUJY',
         'https://amzn.to/3wCu91j']
JYP_img=['https://gd.image-qoo10.jp/li/826/289/4597289826.g_400-w-st_g.jpg',
         'https://gd.image-qoo10.jp/li/538/803/5532803538.g_400-w-st_g.jpg',
         'https://gd.image-qoo10.jp/li/164/917/5205917164.g_400-w-st_g.jpg']
JYP_qoo10_intro=['【TWICE】サナpickアイテム',
           '【TWICE】モモpickアイテム',
           '【Stray Kids】リノ愛用香水']
JYP_amz_intro=['【TWICE】サナ愛用香水',
           '【TWICE】モモpickアイテム',
           '【Stray Kids】ヒョンジン愛用香水']

SM_qoo10_url=['https://www.qoo10.jp/su/1410615174/Q189976361',
        'https://www.qoo10.jp/su/1410615402/Q189976361',
        'https://www.qoo10.jp/su/1410615728/Q189976361']
SM_amz_url=['https://amzn.to/48UGsUp',
        'https://amzn.to/4c1WIFw',
        'https://amzn.to/49AgKpi']
SM_img=['https://gd.image-qoo10.jp/li/506/091/5530091506.g_400-w-st_g.jpg',
        'https://gd.image-qoo10.jp/li/320/398/5532398320.g_400-w-st_g.jpg',
        'https://gd.image-qoo10.jp/li/817/863/5517863817.g_400-w-st_g.jpg']
SM_qoo10_intro=['【NCT127】ジェヒョンpickアイテム',
          '【aespa】ウィンターpickアイテム',
          '【RIIZE】pickアイテム']
SM_amz_intro=['【NCT127】ジェヒョンpickアイテム',
          '【aespa】ウィンターpickアイテム',
          '【RIIZE】pickアイテム']

STARSHIP_qoo10_url=['https://www.qoo10.jp/su/1410610331/Q189976361',
               'https://www.qoo10.jp/su/1410606134/Q189976361',
               'https://www.qoo10.jp/su/1410612854/Q189976361' ]
STARSHIP_amz_url=['https://amzn.to/3P6A4Sy',
                  'https://amzn.to/436tOA7',
               'https://amzn.to/49AgWow' ]
STARSHIP_img=['https://gd.image-qoo10.jp/li/637/469/4933469637.g_400-w-st_g.jpg',
              'https://gd.image-qoo10.jp/li/469/522/5523522469.g_400-w-st_g.jpg',
              'https://gd.image-qoo10.jp/li/592/420/5534420592.g_400-w-st_g.jpg']
STARSHIP_qoo10_intro=['【IVE】ウォニョンpickアイテム',
               '【IVE】ウォニョンpickアイテム',
               '【IVE】ユジンpickアイテム']
STARSHIP_amz_intro=['【IVE】ウォニョンpickアイテム',
               '【IVE】ウォニョンpickアイテム',
               '【IVE】ユジンpickアイテム']

YG_qoo10_url=['https://www.qoo10.jp/su/1410618278/Q189976361',
        'https://www.qoo10.jp/su/1410618438/Q189976361',
        'https://www.qoo10.jp/su/1410618584/Q189976361']
YG_amz_url=['https://www.amazon.co.jp/dp/B0BN7PY6RY/ref=cm_sw_r_as_gl_api_gl_i_PP40BH1KH6YCWDXRVMHY?linkCode=ml1&tag=fromkpopsto-22',
        'https://www.amazon.co.jp/dp/B07JP596F5/ref=cm_sw_r_as_gl_api_gl_i_5X3FRG6683967VZ2CKHV?linkCode=ml2&tag=fromkpopsto-22',
        'https://amzn.to/3uXsi6S']
YG_img=['https://gd.image-qoo10.jp/li/063/923/5473923063.g_400-w-st_g.jpg',
        'https://gd.image-qoo10.jp/li/205/299/5021299205.g_400-w-st_g.jpg',
        'https://gd.image-qoo10.jp/li/361/759/5521759361.g_400-w-st_g.jpg']
YG_qoo10_intro=['【BLACKPINK】ジェニ愛用香水',
          '【BLACKPINK】ロゼ愛用アイテム',
          '【BLACKPINK】リサ愛用アイテム']
YG_amz_intro=['【BLACKPINK】ジェニ愛用香水',
          '【BLACKPINK】ロゼ愛用アイテム',
          '【BLACKPINK】リサ愛用アイテム']

ad_urls=['https://www.qoo10.jp/su/1410613787/Q189976361', 'https://www.qoo10.jp/su/1410615402/Q189976361', 'https://www.qoo10.jp/su/1410612854/Q189976361']
ad_imgs=['https://gd.image-qoo10.jp/li/741/855/5445855741.g_400-w-st_g.jpg', 'https://gd.image-qoo10.jp/li/320/398/5532398320.g_400-w-st_g.jpg', 'https://gd.image-qoo10.jp/li/592/420/5534420592.g_400-w-st_g.jpg']

qoo10_url_dic = {'HYBE':HYBE_qoo10_url, 'JYP':JYP_qoo10_url, 'SM':SM_qoo10_url, 'STARSHIP':STARSHIP_qoo10_url , 'YG':YG_qoo10_url}
amz_url_dic = {'HYBE':HYBE_amz_url, 'JYP':JYP_amz_url, 'SM':SM_amz_url, 'STARSHIP':STARSHIP_amz_url , 'YG':YG_amz_url}
img_dic = {'HYBE':HYBE_img, 'JYP':JYP_img, 'SM':SM_img, 'STARSHIP':STARSHIP_img , 'YG':YG_img}
qoo10_intro_dic = {'HYBE':HYBE_qoo10_intro, 'JYP':JYP_qoo10_intro, 'SM':SM_qoo10_intro, 'STARSHIP':STARSHIP_qoo10_intro , 'YG':YG_qoo10_intro}
amz_intro_dic = {'HYBE':HYBE_amz_intro, 'JYP':JYP_amz_intro, 'SM':SM_amz_intro, 'STARSHIP':STARSHIP_amz_intro , 'YG':YG_amz_intro}




#替え用のHTML
"""
<div class='shr_item' style='position:relative; min-height:158px; margin:12px 0; padding:9px 10px; border:1px solid #dbdbdb; border-radius:1px; background-color:#fff;'>
    <div class='item_dtl' style='position:relative; height:158px; padding:5px; border:1px solid #f0f1f4;'>
        <span class='thmb' style='float:left; overflow:hidden; width:156px; height:156px; margin-right:9px; border:1px solid #e7e7e7;'>
            <a href={urls[i]}>
                <img src={imgs[i]} width='156' alt='' style='vertical-align: middle; border: 0 none;'>
            </a>
        </span>
            <p class='tit' style='overflow:hidden; max-height:68px; margin-bottom:7px; line-height:17px; color:#000;'>
                [Qoo10] {intros[i]}
            </p>
        <span class='url' style='position:absolute; left:170px; bottom:10px; display:block; font-weight:bold; color:#9197a3;'>
            WWW.QOO10.JP
        </span>
    </div>
</div>
"""

"""
<div class='shr_item' style='position:relative; min-height:158px; margin:12px 0; padding:9px 10px; border:1px solid #dbdbdb; border-radius:1px; background-color:#fff;'>
    <div class='item_dtl' style='position:relative; height:158px; padding:5px; border:1px solid #f0f1f4;'>
        <a href={urls[i]}>
            <p class='tit' style='overflow:hidden; max-height:68px; margin-bottom:7px; line-height:17px; color:#000;'>
                [Qoo10] {intros[i]}
            </p>
        </a>
    </div>
</div>
"""