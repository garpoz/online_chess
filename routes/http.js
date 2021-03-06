//baba-god
//garpozir@gmail.com

//var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

const invurl=require('url')
const invfs=require('fs')
const invpath=require('path')
let address=invpath.resolve("./")
address+='/public/contact.json'
const jsonFile=require(address)
var DB = null;

/**
 * Validate session data for "Game" page
 * Returns valid data on success or null on failure
 */
var validateGame = function(req) {

  // These must exist
  if (!req.session.gameID)      { return null; }
  if (!req.session.playerColor) { return null; }
  if (!req.session.playerName)  { return null; }
  if (!req.params.id)           { return null; }

  // These must match
  if (req.session.gameID !== req.params.id) { return null; }

  return {
    gameID      : req.session.gameID,
    playerColor : req.session.playerColor,
    playerName  : req.session.playerName
  };
};

/**
 * Validate "Start Game" form input
 * Returns valid data on success or null on failure
 */
var validateStartGame = function(req) {

  // These must exist
  if (!req.body['player-color']) { return null; }

  // Player Color must be 'white' or 'black'
  if (req.body['player-color'] !== 'white' && req.body['player-color'] !== 'black') { return null; }
var pname=req.body['player-name'];
    module.exports={ pname,  };
  // If Player Name consists only of whitespace, set as 'Player 1'
  if (/^\s*$/.test(req.body['player-name'])) { req.body['player-name'] = 'make'; }

  return {
    playerColor : req.body['player-color'],
    playerName  : 'make',//req.body['player-color']
    pname:req.body['player-name'],
  };
};

/**
 * Validate "Join Game" form input
 * Returns valid data on success or null on failure
 */
var validateJoinGame = function(req) {

  // These must exist
  if (!req.body['game-id']) { return null; }

  // If Game ID consists of only whitespace, return null
  if (/^\s*$/.test(req.body['game-id'])) { return null; }

  // If Player Name consists only of whitespace, set as 'Player 2'
  if (/^\s*$/.test(req.body['player-name'])) { req.body['player-name'] = 'join'; }
  //if (/^\s*$/.test(req.body['player-name'])) { req.body['player-name'] = 'Player 2'; }

  return {
    gameID      : req.body['game-id'],
    //playerName  : req.body['player-name']
    playerName  : 'join'//req.body['player-name']
  };
};

/**
 * Render "Home" Page
 */
var home = function(req, res) {

  // Welcome
  res.render('home');
};
var practice=function(req,res){
  res.render('practice');
}
var invitation=function(req,res){
    let urlObj=invurl.parse(req.url,true);
    urlObj=urlObj.query['invitation']
    let findGml=jsonFile.member[urlObj]
    if(findGml===undefined){
res.set('Content-Type', 'text/html');
    res.write('<title>Online Chess</title>');
    res.write('<h3 style="color:red">invalid invitation code...</h3>');
    res.write('<a href="http://playchesscoin.com" style="text-align:center; background-color:blue; border-radius:9px; border-color:white; padding:12px; font-size:12px; color:white; text-decoration: none ">playchesscoin.com</h3>');
    res.end();
    }else{
            //var xhr=new XMLHttpRequest();
            //xhr.open('GET',`/?validinvitation=${urlObj}`);
            //xhr.setRequestHeader('content-Type','application/json');
            //xhr.send();
        invfs.writeFile('./invitation.txt', urlObj, function (err) {
              if(err){return;}
        });
        res.redirect('/'); return;
    }
}
/**
 * Render "Game" Page (or redirect to home page if session is invalid)
 */
var game = function(req, res) {

  // Validate session data
  var validData = validateGame(req);
  if (!validData) { res.redirect('/'); return; }

  // Render the game page
  res.render('game', validData);
};

/**
 * Process "Start Game" form submission
 * Redirects to game page on success or home page on failure
 */
var startGame = function(req, res) {

  // Create a new session
  req.session.regenerate(function(err) {
    if (err) { res.redirect('/'); return; }

    // Validate form input
    var validData = validateStartGame(req);
    if (!validData) { res.redirect('/'); return; }

    // Create new game
    var gameID = DB.add(validData);

    // Save data to session
    req.session.gameID      = gameID;
    req.session.playerColor = validData.playerColor;
    req.session.playerName  = validData.playerName;

    // Redirect to game page
    res.redirect('/game/'+gameID);
  });
};

/**
 * Process "Join Game" form submission
 * Redirects to game page on success or home page on failure
 */
var joinGame = function(req, res) {

    var ldc=require('./socket.js');
  // Create a new session////////////////////////////
    var kari=Object.values(ldc)
    var kariset=[... new Set(kari)]
    //delete (kar["please"])
    function getKeyByValue(object, value) {
          return Object.keys(object).find(key => object[key] === value);
    }
/////////////////////////////////////////////
  req.session.regenerate(function(err) {
    if (err) { res.redirect('/'); return; }
    // Validate form input
    var validData = validateJoinGame(req);
    if (!validData) { res.redirect('/'); return; }

    var isLargeNumber = element => element == validData.gameID;
    var found = kariset.findIndex(isLargeNumber)
      if (found===-1) { res.redirect('/'); return;}else{
validData.gameID=getKeyByValue(ldc,validData.gameID);
      }
    // Find specified game
    var game = DB.find(validData.gameID);
    if (!game) { res.redirect('/'); return;}

    // Determine which player (color) to join as
    var joinColor = (game.players[0].joined) ? game.players[1].color : game.players[0].color;

    // Save data to session
    req.session.gameID      = validData.gameID;
    req.session.playerColor = joinColor;
    req.session.playerName  = validData.playerName;

    // Redirect to game page
    res.redirect('/game/'+validData.gameID);
    module.exports= validData.gameID;
  });
};

/**
 * Redirect non-existent routes to the home page
 */
var invalid = function(req, res) {

  // Go home HTTP request, you're drunk
  res.redirect('/');
};

/**
 * Attach route handlers to the app
 */
exports.attach = function(app, db) {
  DB = db;

  app.get('/',         home);
  app.get('/practice',         practice);
  app.get('/invitation',         invitation);
  app.get('/game/:id', game);
  app.post('/start',   startGame);
  app.post('/join',    joinGame);
  app.all('*',         invalid);
};
