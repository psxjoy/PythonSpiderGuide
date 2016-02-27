import requests
# 监控摩洛哥精油是否上架，一旦上架发给老姐的手机上

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/48.0.2564.109 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'_uuid=39079e34-7269-4d3b-a672-c1f59086d9cc;'
             ' __da=-215504379541777;'
             ' OZ_1U_2363=vid=v6d04247d8202b.0&ctime=1456490248&ltime=1456490243;'
             ' _jzqx=1.1455543702.1456498125.3.jzqsr=fengqu%2Ecom|jzqct=/detail/10780%2Ehtml.jzqsr=fengqu%2Ecom|jzqct=/detail/10780%2Ehtml;'
             ' CNZZDATA1256288985=1199591736-1455542262-http%253A%252F%252Fwww.smzdm.com%252F%7C1456499244;'
             ' CNZZDATA1256279840=156634024-1455541244-http%253A%252F%252Fwww.fengqu.com%252F%7C1456495387;'
             ' _jzqy=1.1456484530.1456573705.1.jzqsr=baidu.-; '
             '_jzqckmp=1;'
             ' _qzja=1.164100432.1455543702200.1456498125306.1456573704670.1456577134403.1456577787169.0.0.0.66.6;'
             ' _qzjb=1.1456573704670.13.0.0.0; _qzjc=1;'
             ' _qzjto=13.1.0; _gat_UA-62706183-1=1;'
             ' OZ_1U_2295=vid=v6c1d597308ae2.0&ctime=1456577787&ltime=1456577134;'
             ' OZ_1Y_2295=erefer=http%3A//www.v2ex.com/t/259530&eurl=http%3A//www.fengqu.com/detail/10780.html%3F_spm%3D0.sere0.0.3&etime=1456577787&ctime=1456577787&ltime=1456577134&compid=2295;'
             ' _ga=GA1.2.379386047.1455543703; _gat=1; tmc=12.44792627.23507604.1456573704972.1456577134824.1456577788347;'
             ' tma=44792627.55423659.1455545817493.1456484534220.1456573704980.3;'
             ' tmd=59.44792627.55423659.1455545817493.;'
             ' bfd_s=44792627.34495851.1456573704968;'
             ' bfd_g=b1edecf4bbe4880400007449000045ae56c1dddb;'
             ' _jzqa=1.4354667487562971600.1455543702.1456498125.1456573705.6;'
             ' _jzqc=1; _jzqb=1.18.10.1456573705.0;'
             ' _fmdata=99B3EEF20C227339CCC2B93CA24A64E3CE5D86362CD69E984D8ADFD8C8E255226AA2F0AE247D6FB6CF2C6686FC7C5BDDDE12F0222C23A4A3'
}
datas = {
    '_mt':'b2cmall.getProductHotData',
    'itemId':'10780',
    '_sm':'md5',
    '_aid':'1',
    '_sig':'5fc1d3ab173bb79b8dd05df36867bc70'
}

url = requests.post('http://www.fengqu.com/m.api',data = datas,headers = header)
print(url.json())
