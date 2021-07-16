# Cloudflare DDoS Protection Case-Study
Case Study of Cloudflare DDoS Protection

![Cloudflare DDoS](src/ddos.gif)

1. Request to 'https://deerequipment.com/wp-json/cnb/v1/equipment/in-stock/used' with respone 503 and index.html
- _cf_chl_opt
```javascript
window._cf_chl_opt={
  cvId: "2",
  cType: "non-interactive",
  cNounce: "86454",
  cRay: "66bcf45b2880e910",
  cHash: "bbe0ba7eac360e3",
  cFPWv: "b",
  cTTimeMs: "4000",
  cRq: {
    ru: "aHR0cHM6Ly9kZWVyZXF1aXBtZW50LmNvbS93cC1qc29uL2NuYi92MS9lcXVpcG1lbnQvaW4tc3RvY2svdXNlZA==",
    ra: "TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkxLjAuNDQ3Mi4xMjQgU2FmYXJpLzUzNy4zNg==",
    rm: "R0VU",
    d: "tGJ4s3EWIcMPz+x+msFVN3nfhUKH/NpiDkfiFj/CDHfzpqnc8pxinKilnNEwie8FKXN66YA9Z6RcbO+WPXDQiRs5ATEjOPlfJ+CmytT7v4aogVv+vGJqRvj0LCnB8hfjzUi6xwvSDgSeJm/kJ+9nvRXy5H3fzaNnN0I3y423q93UDDnBsjKWbN7OMcTLHVkqxeojGHT1Kpk2JjfbqJiPRgc47S/TNvG6eHyW/gUCaOffc6U540000gnqbLVbcC8swlOXklPK/CcCHM3MAkbV/HzZvOii2xh0ptR7RvWTML/Yk1IL1wUiZEMqIJIDXdyy373P9PMKhy9ZOO1eRvxvSmOm+z99QzObJ2nY24PnqA8V58NI9Aqa2ez2vyUPquWiEPy6qD+PBz4dwM1YxYh1MK84epBipeY7sfuLoyNA1UaX0wDi0DMIfOsjE8/KPSerrtgI4vxeTBtEwuY1hzErQUKo9DGPQ1Qx4UfI21clJbFGRG8KmSbsG1DYmUHrKfwbiep0OlDKXvzJGg5kP7sTPuoiDJfTxeECfIezN255Ol29fBbpN79GnVe6IyKUZfIDzRVfTkgTmbd2t0itB+TMCmHHbG9zkIy/FbA2XtW4ExF9J5S7YjXVrCjmr0zsimQqoS4Rbyx7h44/y+qacLma3/dQXUEF5YYd5wovBzXckGaaJ/xlRp8tsOE23c/Tm19pBuMVvkHr44SqGAIB+h5dnw==",
    t: "MTYyNTc4NTQ5Ni44MjYwMDA=",
    m: "CVKqPxHDjuc6bxRcORbo01Jqcin35k36YrbXsXUZKAg=",
    i1: "MsuhWXaJwqk5gLKhsJEiJQ==",
    i2: "shhRhDLzcztg1YXQqM6YCg==",
    zh: "RNA188MYEsT+EXAiRJOuTfvXanOGCBUiPx47TQHk+CQ=",
    uh: "6MfvW9btGmDtSIPzr0zj9JhmieeaNz5tOYKoqhCmfqk=",
    hh: "TcdWAoEmBZlx5hKi4JOnuGvLj80gOFefaEVJsYrULrQ=",
  }
}

```
- Challenge Form

```html
<form class="challenge-form" id="challenge-form" action="/wp-json/cnb/v1/equipment/in-stock/used?__cf_chl_jschl_tk__=f8d38707746b17a9e36e3476807e9ac96cfb2f87-1625785496-0-AUVWLkNMoY7_BYyID3lZZin3ddFtvODijtBo0k6_8P92QpGc7S9da9Sru8WHyl-1724ApuJWXSsgU3ERL7hgCqTCXcJqBwJemONJa_ZISdMqnCWTTUqJO20VRxgh9KZH9FktGcaTqfgWmWWO9dsvH0ITF45GagPYBqn6HNFo880-KYmOrjNdMvDBZuFUXdHPxjiPRScXYi-oY2QgA4KIjwy8SmhjgsXFQg60MUbqlqTODSWsWIDxGgNY3TQBKM3kzyMJzOo64EXFtOsYskKw6hekL7P_1gRiKS5-t0ySR1RY4ubgbEyGqy2AVtL7h3UbxA9x0qUe1llrTWj4TvMR-ikRwxZ2YPoHGIy9RK9A_wIdKZ2iYh3BYj1l1YZYuA4MXbxKXr0HgbGSk-QHZ2RCdvEXKLXwnlyc5vXWC8Xfzu82rGiwCSWdOBDr6B3LvFajlJLuLLdxz7NMAb97ClmUXMSLbM86cde55DnK2e7HYYAKeOUvnLih9vD0UBCxOkP7jg" method="POST" enctype="application/x-www-form-urlencoded">
  <input type="hidden" name="r" value="e05f09c2a8c376c82fba27ffe747b2b6eadce81a-1625785496-0-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"/>
  <input type="hidden" value="7b321ad75b75e93a95f2ddec9882366d" id="jschl-vc" name="jschl_vc"/>
  <!-- <input type="hidden" value="" id="jschl-vc" name="jschl_vc"/> -->
  <input type="hidden" name="pass" value="1625785500.826-wzKRyGlGEQ"/>
  <input type="hidden" id="jschl-answer" name="jschl_answer"/>
</form>  
```
2 -  send request to https://deerequipment.com/cdn-cgi/challenge-platform/h/b/orchestrate/jsch/v1?ray=66bcf45b2880e910 to get the js code handle the redirect process return 200 and code.js file
```javascript
b = 'GxbYe,NKeEK,Vpums,isHaj,VYNOJ,null,<div class="yjs-content"><p style="background-color: #de5052; border-color: #521010; color: #fff;" class="cf-alert cf-alert-error">&#35813;&#32593;&#31449;&#36164;&#28304;&#26080;&#27861;&#36890;&#36807;&#27492;&#22320;&#22336;&#35775;&#38382;&#12290;</p></div>,2|5|0|4|1|3,pJTcT,dUZaw,pMGYI,console,XLikf,WnxQd,kXIIz,KdqfX,HGkdE,CLcvL,rPiev,jiRfL,send,call,display,XPkSi,Error object: ,BKbrz,uKvFp,TCbuo,tCVsb,chCAS,MHajj,jc-content,cookie,xOogh,apply,qVsGJ,ySfuA,cf_chl_,object,CKylC,prototype,fsDZz,CUQri,JGqyJ,getUTCMinutes,complete,izVqB,DOMContentLoaded,Date,charCodeAt,parseInt,toLowerCase,<div class="jc-content"><p style="background-color: #de5052; border-color: #521010; color: #fff;" class="jc-alert jc-alert-error">&#35813;&#32593;&#31449;&#36164;&#28304;&#26080;&#27861;&#36890;&#36807;&#27492;&#22320;&#22336;&#35775;&#38382;&#12290;</p></div>,NuHTB,XjSHb,kVfSz,lwPLq,Math,vGwbe,VYCtY,VxmYT,iVwZR,cf-please-wait,yIiom,HhsKR,navigator,UxYER,OdRNd,UBnSW,PaoqW,OkvbL,WpjOC,RdpGs,dMdEn,readystatechange,hostname,forEach,EIjLs,cTTimeMs,QgjOM,jdrFE,aIDrT,dXOHq,challenge-form,TnuLy,TCaZP,onreadystatechange,iVIkE,JKLMt,xdTyu,mijxA,expires=,cImoT,pVUVs,HscGH,qXkdf,_cf_atob,KZoQw,Column: ,qvtUN,split,nEnmY,WEDij,kHVeF,KyOYF,substring,bSHlP,flow/ov,EaVBC,VGOCnLQd,URL: ,Yzbux,tCnQF,script error,NJzrG,getUTCHours,string,fiIAe,LytTN,_cf_chl_done_ran,[[[ERROR]]]:,AywuD,PhUWc,toJSON,wPdCp,JAOUn,pXtlB,POST,fqPDz,rJILV,cf-content,Pstbq,WHwMP,test,VYLiZ,kdrxu,toString,yNkNG,zpwvx,fENZm,dAIXO,YaxWj,setTime,FLlCo,cvId,jbDiJ,AuEaL,atob,chiRX,UTmZN,Utkdp,_cf_chl_done,OrGFa,rsScB,cf_chl_rc_ni,JnqJt,location,getUTCFullYear,responseText,Bhfbf,Microsoft.XMLHTTP,akkDn,QuuYB,bmrpW,Message: ,nuJQt,0000,qvYfF,===,BWYfF,saqZY,DXpsZ,ytrVG,<div class="cf-content"><p style="background-color: #de5052; border-color: #521010; color: #fff;" class="cf-alert cf-alert-error">This web property is not accessible via this address.</p></div>,cNounce,attachEvent,sendRequest,USsWR,TpYFB,SHA256,NzjtS,cLt,bnmDq,JSON.parse,saqSd,hasOwnProperty,/0.2281579673964972:1625784938:3707080a78fc301bc990971269688e856e3b796bc94633cec3bbc5e6ce71a5d2/,LcdpX,ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=,KEyCX,getUTCSeconds,vhhxA,mqroM,kdOAv,XUXLs,rjmvB,charAt,iEfif,sDvaY,oOkMi,XMLHttpRequest,qRtls,number,_cf_chl_enter,UsKvA,sHEyP,lceYw,yBvev,Function,LDkZq,YKWoH,oTVhr,LwKWA,AwqIWrdXBZhJU$DYaN4ifRglQKk87mHv6VC0-xPGM291szEypnbeTtLSO3o5cjF+u,CKCJj,RsYce,pghJB,bevye,vuzhG,xHbpK,JKijj,hvHAp,cZZXC,zzyeG,HoLph,chReq,EDtjN,rJyHV,VkSYD,nNyXE,hkhvn,leVcL,olWcP,FETMp,BArns,dHwPt,cRq,log,location-mismatch-warning,clGIt,Content-type,sUNSl,HzTXO,sTYIt,onerror,etlou,slice,tTjgm,PxCGs,FValt,JpXYx,rEYYn,PuQVC,pow,glLRZ,fnZWQ,UEOZu,getTime,open,zOgkC,GCEDE,FhLym,sIoSd,fromCharCode,join,getUTCMonth,dycyY,gIUgx,aPABj,toiaJ,NmXGG, - ,cGzhi,NKofn,kxWzH,UYbMWAJeHfVrvE4dBtPmXjI6oQ1k9uTCxi8OGLzgypwDZn35cSqKRN0l2ahF7s,kwaqx,JLyid,indexOf,boolean,CyCcW,jc-please-wait,setTimeout,eSWDV,aeLzw,fshFh,min,yjs-content,Line: ,KwUBl,_cf_chl_ctx,gANtT,avZpZ,oPKqh,cType,protocol,pFDoD,XrMjh,stringify,PdDyG,qGIGx,gvHXn,SxbFIBdVESgY,oecfi,ldkry,IHbuu,readyState,EvtYL,0123456789abcdef,QQoWB,application/x-www-form-urlencoded,kfjIp,no-cookie-warning,getUTCDate,replace,length,qNJtB,poFCy,block,BoYnL,SQFuC,sVJyu,MDESk,FcZAk,OZXsM,cHash,dHjby,wjsiQ,addEventListener,mjOOh,ykjpz,EWftm,Xvhha,FRjqc,getElementById,wjekW,shrBW,timeout,setRequestHeader,createElement,nCnjQ,nxUyu,status,MNawV,kyOuD,IRHRx,PsHRw,PaRZK,=; Max-Age=-99999999;,QQTyR,cf_chl_prog,parse,GfwLj,VkYbb,alert,UCPBB,xcQIJ,ontimeout,yGgOq,WOZuz,xUtlj,tyIrL,mVpuy,Oqjbq,DSjYX,chC,reload,aWdfq,FFBfO,qBmLy,ZFSSj,LJoPy,RyyXt,GMlqL,mRrYm,cFPWv,lPpEM,ActiveXObject,UDKbg,Script Error: See Browser Console for Detail,iMSaA,toUTCString,pkRXa,JpdGx,sSnfs,;path=/,fnNin,pqwyf,3|4|2|1|0,3|5|1|0|2|4,FSqGP,NELiO,loaded,JSON.stringify,qSAEN,AyMvp,function,dmAQV,QPhqs,kAOUB,eGyTV,This browser is not supported.,WCyfL,ybMWQ,href,push,[object Array],0|1|3|2|4,style,type,fkmZZ,bZlxU,ldahb,innerHTML,JSON,HjIrk,cRay,TNrls,IFhUi,TmJcU,MBOQo,WXQAe,xyUZN,MsHIm,cookieEnabled,wRalx,KlZgO,Fgugn,/cdn-cgi/challenge-platform/,jgCzB,aaroE,4|2|0|3|1,xqySK,lastIndex,DWRxE,_cf_chl_opt,valueOf,interactive,YqNgf'.split(','),
    function(a, c, d) {d = function(e) {for (; --e; a['push'](a['shift']()));}, d(++c)}
    (b, 345), 
    c = function(a, d) {
        var e;
        return a = a - 0, e = b[a], e
    }
 ```
after preparing the code using python script prepare_js_code.py to replace all c('0xX') with the b list value and we get code_after.js ready to run
Example
```javascript
t[c('0x1b')] to t['RyyXt'] 
```
3- post requests to https://deerequipment.com/cdn-cgi/challenge-platform/h/b/flow/ov1/0.2281579673964972:1625784938:3707080a78fc301bc990971269688e856e3b796bc94633cec3bbc5e6ce71a5d2/66bcf45b2880e910/bbe0ba7eac360e3 response 200 using this function of code.js or code_after.js
with header 
CF-Challenge: bbe0ba7eac360e3
Content-type: application/x-www-form-urlencoded
and body 
v_66bcf45b2880e910: $OB6n6r646260CAlqAm6Hnag6ZQMqOpwDAVPXz6dOp6ATOA7P6hO20lBA7A8AqpqsYgEAMwZAqKBaAZCdaAp-6AUmHaWWAb-12MAk-6qUh9A-4Vqi47aA4fNgqswKJ6w-AG6WOAt6qTAo0zmyAATAUltCBBAVYIcFNg7AgSMhAq$tmpwPUIxjDIA2mbKGhlMPAWtsmb-XmBA8UqqmAA7pAXrjg24fAWfhQxcHYIAU9AMb9awGq0W6Fx1yRawHNkW44aARlS7EvMAYq8JtIGtGAqzRAXUAkNqnZ24WT8WUVpytLEoJVSlRZ67AWaPrnTfx9iXM2LoAXQNrQJCf3ZOJzTM6wSrhzXNwYpAhg7WRojXgI6bKp7fVW766eGfB46NJ-9BEd$9Vdco-CR0cjWBhR74Dof661V4f6oe6Al23mPmvyN+zTlz6HJsXZqJ6wRhaVwZxBBO2940f4FCEX6PC5JRQZ44LXakMa4KwORMOG6iIBAfRcB0AI6AqVhA$45BUZqQVXiTIBMAwPWAtRbsAX2oWtsYjYJXsqrisP3Yc1JdZfTOhpDWtm161zVkCVoZ5fm6QwpaxmKxpEdRRD3yrpMdAf6w3BDFvtwwlQhAiYC9mkHT3I LtgUOM$bwhEYI1hWfX0W$IACVwCCEEq0f5nDaM4B7qqnTO40lQJC5RWfmi q59dAOVJZeptS7rAhq6BZlIOhpUPJQVoX1NaNAbUT2AbDwU6tv3 VyqKiCElpfGMhWVp7UwtP7hpmWcDwmV6$wixkhntGThOP-cha7RDgUf06XrsXjhAJ0AX6MlfK$tP4RMEw6hnlrcK$$i-Q6Vt0gUpqOIfwWfJirAErAOw4Kpmw48BDAPRrkCXBZYr9vT1Ge8ZXwHRNYw4XN-bsqRyAMBmsdphNm66NaP0phAMRdlnCg7KUb-cvaNd7vNfgv8nYa7DANwnWN CqUNlr7IBMabvtSXjwp1PrlsVbXvaQrdlQYp4B7WCIqRSX78MZ4XrB74-rwnVOvTj$fI6mIOIVowWmnRI6Q62w6qf2AMRp$ljDAPrc8wYljRpEI6vO6Sj4BZNOUNfa7vabxLUMBXTU9DwOdAP-C8APV6UMMaPgUC0aRnorfva$aCNNflF8wrXFwpNr0B77UjIV-bEvTvTBa6cAEWaHAMd0tPCNzbGTqAZfjaVE-i$wSXFR2 govNExLX6$R0WaniAgM7N4WZgC6RMDqEwZtw4qKLGFUMW6thnqqEg$Tg8Z2rqXg2 G8q6ZNnRMJ0Oin aFjK 4Q$AUnng$tVMeT3qKF8oq-Y6FAR62QTCrBP-BjngVaXaQqOWNlqEIRyqK OZ46XN0kNmQWV4Ua2IpNNsIp4B6LZI71qsIrSqx8S-nqrZRq-BBcAditmVqmp7iOmaMihf3d-BDNi64aVrAxqKsA48MOIamaHq6YxmCVqAHwOK$lqIdkpW4Q6UPiUafatiTa0OUMb0WYVfiaq609qUwYrkQVCwnK$mx9hAP6OYAZCXiTfJAU4WGTmpG1FXahWcqlw fDwgxfWaWO6Y6nwahChTmAcq4dFdfloopVZWPoXpH6bMHw90hdmvO4pVALPaXBXaRpOIFxLrQvO2pPw9N4JsA7aOH3MWfYMXWHN7AKWtV-JsyB66iqqX5hOxpRVTdpYMUwWpPAarcWWvH9BOqHIOw7Kp3fZ6O-j$6XWSN6W6Ic2BqQWwMAaXFZhUAWMTQl4qDSZpKa3qgPO4AqfWw8N lTwpI6I6bCH6PDsBUGM6C9qGICB7iwtCn6MqBxAa3gVbWCUFYwpxt0mqsZOm74CVqqU-rpwpvCz62wmA-vOHwtACWIBSqf2n4OaA4ULdAsWZNcIpWDUMRpTwpA6wEgUO0eWkBLdAUayVRwMWjA-4BSVkC5IOwAdsYAyWMqQhTq6KpDAo4XqWdAsKCqHVTICAOVA$iDwZCsAAyxsMAA
and cookies
cf_chl_2=bbe0ba7eac360e3
cf_chl_prog=e

```javascript
var B, C;
B = 'POST', A['open'](B, u, !![]), x['GxbYe'] in A && (A['timeout'] = 2500, A['ontimeout'] = function() {
    z()
}), A['setRequestHeader'](x['pqwyf'], x['gIUgx']), A['setRequestHeader']('CF-Challenge', d['_cf_chl_opt']['cHash']), A['onreadystatechange'] = function() {
    if (x['BArns'](A['readyState'], 4)) return;
    if (A['status'] != 200 && x['BArns'](A['status'], 304)) return x['hvHAp'](z), void 0;
    q(A), x['FhLym'](n, x['jbDiJ'], x['akkDn']('b', d['_cf_chl_ctx']['chC']), 1), new d[('Function')](decodeURIComponent(g['VGOCnLQd'](h(A['responseText']))))(), x['VYNOJ'](n, x['jbDiJ'], 'a' + d['_cf_chl_ctx']['chC'], 1)
}, C = g['WEDij'](JSON['stringify'](d['_cf_chl_ctx']))['replace']('+', x['FFBfO']), A['send']('v_' + d['_cf_chl_opt']['cRay'] + '=' + C)
```
