angular.module 'starthack'
  .config ($stateProvider, $urlRouterProvider) ->
    'ngInject'
    $stateProvider

      .state 'menu',
        url: '/'
        templateUrl: 'app/views/menu.html'
        controller: 'MenuController'

      .state 'game',
        url: '/game'
        templateUrl: 'app/views/game.html'
        controller: 'GameController'

    $urlRouterProvider.otherwise '/'
