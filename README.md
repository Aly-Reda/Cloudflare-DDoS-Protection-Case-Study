# Cloudflare DDoS Protection Case-Study
Case Study of Cloudflare DDoS Protection

![Cloudflare DDoS](src/ddos.gif)

1. Request to 'https://deerequipment.com/wp-json/cnb/v1/equipment/in-stock/used' with respone 503 and index.html
	a._cf_chl_opt
	![Opt](src/opt.PNG)
	b.Challenge Form
	![form](src/form.PNG)
```html
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
