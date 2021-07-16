# Cloudflare DDoS Protection Case-Study
Case Study of Cloudflare DDoS Protection

![Cloudflare DDoS](src/ddos.gif)

1. Request to 'https://deerequipment.com/wp-json/cnb/v1/equipment/in-stock/used' with respone 503 and index.html
a._cf_chl_opt
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
b.Challenge Form

```html

<form class="challenge-form" id="challenge-form" action="/wp-json/cnb/v1/equipment/in-stock/used?__cf_chl_jschl_tk__=f8d38707746b17a9e36e3476807e9ac96cfb2f87-1625785496-0-AUVWLkNMoY7_BYyID3lZZin3ddFtvODijtBo0k6_8P92QpGc7S9da9Sru8WHyl-1724ApuJWXSsgU3ERL7hgCqTCXcJqBwJemONJa_ZISdMqnCWTTUqJO20VRxgh9KZH9FktGcaTqfgWmWWO9dsvH0ITF45GagPYBqn6HNFo880-KYmOrjNdMvDBZuFUXdHPxjiPRScXYi-oY2QgA4KIjwy8SmhjgsXFQg60MUbqlqTODSWsWIDxGgNY3TQBKM3kzyMJzOo64EXFtOsYskKw6hekL7P_1gRiKS5-t0ySR1RY4ubgbEyGqy2AVtL7h3UbxA9x0qUe1llrTWj4TvMR-ikRwxZ2YPoHGIy9RK9A_wIdKZ2iYh3BYj1l1YZYuA4MXbxKXr0HgbGSk-QHZ2RCdvEXKLXwnlyc5vXWC8Xfzu82rGiwCSWdOBDr6B3LvFajlJLuLLdxz7NMAb97ClmUXMSLbM86cde55DnK2e7HYYAKeOUvnLih9vD0UBCxOkP7jg" method="POST" enctype="application/x-www-form-urlencoded">
<input type="hidden" name="r" value="e05f09c2a8c376c82fba27ffe747b2b6eadce81a-1625785496-0-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"/>
<input type="hidden" value="7b321ad75b75e93a95f2ddec9882366d" id="jschl-vc" name="jschl_vc"/>
<!-- <input type="hidden" value="" id="jschl-vc" name="jschl_vc"/> -->
<input type="hidden" name="pass" value="1625785500.826-wzKRyGlGEQ"/>
<input type="hidden" id="jschl-answer" name="jschl_answer"/>
</form>
     
```
