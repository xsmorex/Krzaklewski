(function(){angular.module("starthack",["ngAnimate","ngCookies","ngTouch","ngSanitize","ngMessages","ngAria","ngResource","ui.router","toastr"])}).call(this),function(){angular.module("starthack").service("MenuStates",function(){return{ENTRY:0,MODE_SELECTION:1,RANKING:2,EXIT:3}}),angular.module("starthack").controller("MenuController",["$scope","MenuStates",function(e,n){return e.menuStates=n,e.state=n.ENTRY,e.main=function(){return e.state=n.ENTRY},e.play=function(t){return t?$state.go("game"):void(e.state=n.MODE_SELECTION)}}])}.call(this),function(){angular.module("starthack").service("Pedal",function(){return{pedalLevels:{0:{range:[0,30],image:"pedal_low.png"},1:{range:[30,50],image:"pedal_medium.png"},2:{range:[50,80],image:"pedal_high.png"},3:{range:[80,100],image:"pedal_veryhigh.png"}},getImage:function(e){var n,t,a,l;for(l=this.pedalLevels,n=0,t=l.length;t>n;n++)if(a=l[n],e>=a.range[0]&&e<=a.range[1])return a.image}}}),angular.module("starthack").service("WebSocket",function(){var e;return e={ws:null,connect:function(n,t){return e.ws=new WebSocket("ws://localhost:8000/"),e.ws.onopen=n,e.ws.onclose=t},handleMessage:function(n){return e.onmessage=n}}}),angular.module("starthack").controller("GameController",["$scope","WebSocket","Pedal",function(e,n,t){var a;e.status="connecting",n.connect(function(){return e.status="connected"},function(){return e.status="disconnected"}),a=0,window.DeviceMotionEvent&&(window.ondevicemotion=function(e){return a=e.accelerationIncludingGravity.z})}])}.call(this),function(){angular.module("starthack").run(["$log",function(e){"ngInject";return e.debug("runBlock end")}])}.call(this),function(){angular.module("starthack").config(["$stateProvider","$urlRouterProvider",function(e,n){"ngInject";return e.state("menu",{url:"/",templateUrl:"app/views/menu.html",controller:"MenuController"}).state("game",{url:"/game",templateUrl:"app/views/game.html",controller:"GameController"}),n.otherwise("/")}])}.call(this),function(){angular.module("starthack").constant("malarkey",malarkey).constant("moment",moment)}.call(this),function(){angular.module("starthack").config(["$logProvider","toastrConfig",function(e,n){"ngInject";return e.debugEnabled(!0),n.allowHtml=!0,n.timeOut=3e3,n.positionClass="toast-top-right",n.preventDuplicates=!0,n.progressBar=!0}])}.call(this),angular.module("starthack").run(["$templateCache",function(e){e.put("app/views/game.html",'<div class="game__message" ng-if="status == \'disconnected\'">DISCONNECTED</div><div class="game" ng-if="status == \'connected\'"><div class="pedal"><img ng-src="{{ pedalImage }}"></div></div>'),e.put("app/views/main.html","- title - menu (arrow control) - background gif? - 1: [ Play Ranking Settings Exit ] 1 -> 2 2: [ Select mode: Real track Simulation ] 2* -> 3 3: [ Please wait for your turn. [ SPECTATOR DISPLAY ] ] 4: [ [ Disconnect ] [ GAMER DISPLAY (po prawej u dołu pedał gazu) ] ]"),e.put("app/views/menu.html",'<div class="menu"><div class="title">TheTrackTroll</div><span ng-show="state == menuStates.ENTRY"><a ng-click="play()">Play</a> <a ng-click="settings()">Settings</a> <a ng-click="ranking()">Ranking</a> <a ng-click="exit()">Exit</a></span> <span ng-show="state == menuStates.MODE_SELECTION"><a ng-click="play(\'real\')">Real mode</a> <a ng-click="exit(\'simulation\')">Simulation</a> <a ng-click="main()">Go back</a></span></div>')}]);
//# sourceMappingURL=../maps/scripts/app-02176e5fd4.js.map
