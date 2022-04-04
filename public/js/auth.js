//baba-god
//garpozir@gmail.com
$('#h-btnbg').hide();
$('#myInput').hide();
function copyToClipboard(text) {
    var sampleTextarea = document.createElement("textarea");
    document.body.appendChild(sampleTextarea);
    sampleTextarea.value = text; //save main text in it
    sampleTextarea.select(); //select textarea contenrs
    document.execCommand("copy");
    document.body.removeChild(sampleTextarea);
}

function myFunction(){
    var copyText = document.getElementById("myInput");
    copyToClipboard(copyText.value);
}

$( ".fasele"  ).on( "click", function() {
    var Much=$('#playerName').val();
    if(Much===''){Much='0';}
    var email=$('#email-name').text();
    if(parseInt(Much)<1){
    }
    if(email.length<17){
    }

} );
$.getJSON("https://api.ipify.org?format=json",(data)=>{
     $("#ip-name").text('Your Ip: '+data.ip);
})
function onSignIn(googleUser) {
      var profile = googleUser.getBasicProfile();
//      var manpageUrl= 'http://www.playchesscoin.com/?invitation='+profile.getEmail()

      localStorage.setItem("gMail",profile.getEmail());

$('#h-btnbg').show();
$('#myInput').show();
      var strg=localStorage.getItem("gMail");
      var manpageUrl= 'http://playchesscoin.com/invitation/?invitation='+strg
$('#myInput').val(manpageUrl);
$('#share-bar').share({
        pageUrl: manpageUrl,

    }
);

     // console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
      console.log('Name: ' + profile.getName());
      console.log('Image URL: ' + profile.getImageUrl());
      console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
    $(":submit").removeAttr("disabled");
$.getJSON('/contact.json',(jd)=>{
    var bl=false;
    Object.keys(jd.member).forEach((key)=>{
        if(key===profile.getEmail()){
            bl=true;
        }
    })
        if(bl===false){
            jd.member[profile.getEmail()]=10;
            const myJSON = JSON.stringify(jd);
            var xhr=new XMLHttpRequest();
            xhr.open('GET',`/?gmail=${profile.getEmail()}`);
            xhr.setRequestHeader('content-Type','application/json');
            xhr.send();
    $('#pool-name').text(`Your Credit: 10`);
            sessionStorage.setItem('contact.json',profile.getEmail());
            document.getElementById("playerName").maxLength=2;
            document.getElementById("gameID").maxLength= 2;

        }else{
            document.getElementById("gameID").maxLength=Number(((jd['member'][profile.getEmail()]).toString()).length);
            document.getElementById("playerName").maxLength=Number(((jd['member'][profile.getEmail()]).toString()).length);

            function separate(Number)
{
Number+= '';
Number= Number.replace(',', '');
x = Number.split('.');
y = x[0];
z= x.length > 1 ? '.' + x[1] : '';
var rgx = /(\d+)(\d{3})/;
while (rgx.test(y))
y= y.replace(rgx, '$1' + ',' + '$2');
return y+ z;
}
var crt=separate(jd['member'][profile.getEmail()])
    $('#pool-name').text(`Your Credit: ${crt}`);
        }
 })

$.getJSON('/contact.json',(jd1)=>{
    $('#email-name').text(`Your Email: ${profile.getEmail()}`);
    $('#id-name').text(`Your Id: ${profile.getName()}`);
})
    $('.hide-button').show();
    $('.hide-button').text('❌Sing Out '+profile.getName());
}
    function signOut() {
            var auth2 = gapi.auth2.getAuthInstance();
        auth2.signOut().then(function () {
    $('.hide-button').hide();
    $('#email-name').text(`Your Email: _`);
    $('#id-name').text(`Your Id: _`);
    $('#pool-name').text(`Your Credit: _`);
            $(":submit").attr("disabled", true);
    //              console.log('User signed out.');

        });

    }
