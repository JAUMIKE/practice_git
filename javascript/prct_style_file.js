//Intent變數設定
msg.IntentName = msg.payload.IntentName;
var PName = msg.payload.parameters
if(PName.length>0)
    PName = JSON.parse(PName);
else
    PName = "";
var iResp = msg.payload.response;

// Intent 前置格式設定
var intent = {
    "name": "",
    "auto": true,
    "contexts": [],
    "responses": [{
        "resetContexts":false,
        "parameters":[{}],
        "message": [{
            "type":0,
            "lang":zh-tw,
            "speech":""
        }]
    }],
    "priority":500000,
    "webhookUsed":false,
    "webhookForSlotFilling":false,
    "fallbackIntent":false
};
intent.responses[0].messages[0].speech = iResp;
intent.name = msg.IntentName;

//User says 前置格式設定
var usersays = [];

//設定HTTP Header
var headers = {
    "content-type":"application/json",
    "Content-Disposition": "attachment; filename=" +msg.IntentName +".json"
};
headers["Content-Disposition"] = "attachment; filename=" + msg.IntentName + ".json";
msg.headers = headers;
msg.intent = intent;
msg.usersays = usersays;
msg.PName = PName;
return msg;