/*
此文件为Node.js专用。其他用户请忽略
 */
//此处填写京东账号cookie。
//注：github action用户cookie填写到Settings-Secrets里面，新增JD_COOKIE，多个账号的cookie使用`&`隔开或者换行
let CookieJDs = [
  '__jdu=16022111943351517893919; shshshfpa=441446bd-f28f-7d7c-102d-b20d4d5df6b5-1602236967; shshshfpb=lje6CsvQd8tRe3Yy3huPVmw%3D%3D; user-key=eefc5716-af90-4a9f-8fbe-7e2caf7c4248; pinId=sEaZjERH_ossWutW9f4kaA; pin=fu254983303; unick=%E5%A4%AB%E5%AD%90%E4%B8%B6%E5%88%AB%E7%8A%AF%E8%B4%B1; _tp=klwAnJTY3QUrxzBAOhVKug%3D%3D; _pst=fu254983303; unpl=V2_ZzNtbRBVE0Z9DhZSckxcVmIBR1gSBBcQdggUB3kZWwJuVkUIclRCFnQURlRnGFgUZAIZXkpcQhVFCEdkexhdBGEHGl5CUXMlRQtGZHopXAJmABFdQldLEHcKQlR%2fGVoMbwEaXUpncxJ1AXZSfhtaAm8CIgYXOUQVJQBDVXgRCQVlBkdtQlJKEXMLQlF4EWwEVwMWVERVRBZzAUZkMHddSGcEE15BV0MVfQ1EVn8ZWAVhChpfSldLJXMNRFJ8EV01ZA%3d%3d; __jdv=122270672|www.yirlir.com|t_1000759217_|tuiguang|c3ab97a78d1b43d4abe421cb31668dfd|1604579342710; cn=5; shshshfp=a4de1f91824c6c9104474402ca00442d; areaId=17; ipLoc-djd=17-1381-50720-0; PCSYCityID=CN_420000_420100_420112; __jda=122270672.16022111943351517893919.1602211194.1605582884.1605687142.44; __jdc=122270672; 3AB9D23F7A4B3C9B=3T6OZ5LBZ4MU62TNGMKVZ74DGHNHFB2X6MQEIKUNZ4LZO4X7EXNAIBGPJN3XVVBSMBZC6UK7L7LAANJANK25E6BAJ4; wlfstk_smdl=b8im9c3zsgpaqyl6jcdzge54srismjqy; TrackID=1TyMbAndE5Ph2YF-Zk7ntP8D5GjdVddDhGwpNL1CGxXLVbEY_ETL5Duvxn0FbDLD3m9ssFpuC23kFd0G5XD2TBBK_ZGMeemUWJRZu7spGjrs; thor=34AC5F574230EC877B2D4D6E79A836BB80EC25EB150CF9D9375F9723452763CA1673BE1C074A31F149DD0B7D092E204DA9B1D2B28F736C7E599960943C571E5F181D7BC36E21C18773203F7392CAD59EDD27835C1049BCA31D33D55D33A33872226DC5345082B4C71AE9173A93329C0A08C3104CF4066BA38BB32F4D3739C939CD203F77D2B771894C49A3D06AAFDA20; ceshi3.com=201; shshshsID=024a3ce3a2161a1129f57fe9b71f6f78_2_1605687164317; list_sign_-1830731356=66cfc083121a8a7154356170cf42a6bd; __jdb=122270672.6.16022111943351517893919|44.1605687142',//账号一ck,例:pt_key=XXX;pt_pin=XXX;
  '',//账号二ck,例:pt_key=XXX;pt_pin=XXX;如有更多,依次类推
]
// 判断github action里面是否有京东ck
if (process.env.JD_COOKIE) {
  if (process.env.JD_COOKIE.indexOf('&') > -1) {
    console.log(`您的cookie选择的是用&隔开\n`)
    CookieJDs = process.env.JD_COOKIE.split('&');
  } else if (process.env.JD_COOKIE.indexOf('\n') > -1) {
    console.log(`您的cookie选择的是用换行隔开\n`)
    CookieJDs = process.env.JD_COOKIE.split('\n');
  } else {
    CookieJDs = process.env.JD_COOKIE.split();
  }
  console.log(`\n====================共有${CookieJDs.length}个京东账号Cookie=========\n`);
  console.log(`==================脚本执行- 北京时间(UTC+8)：${new Date(new Date().getTime() + new Date().getTimezoneOffset()*60*1000 + 8*60*60*1000).toLocaleString()}=====================\n`)
  // console.log(`\n==================脚本执行来自 github action=====================\n`)
}
for (let i = 0; i < CookieJDs.length; i++) {
  const index = (i + 1 === 1) ? '' : (i + 1);
  exports['CookieJD' + index] = CookieJDs[i];
}
