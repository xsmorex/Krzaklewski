angular.module 'starthack'
  .service 'Pedal', ->
    pedalLevels:
      0: range: [0, 30], image: 'pedal_low.png'
      1: range: [30, 50], image: 'pedal_medium.png'
      2: range: [50, 80], image: 'pedal_high.png'
      3: range: [80, 100], image: 'pedal_veryhigh.png'

    getImage: (acceleration) ->
      for level in @pedalLevels
        if acceleration >= level.range[0] and acceleration <= level.range[1]
          return level.image

angular.module 'starthack'
  .service 'WebSocket', ->

    wsService =
      ws: null
      connect: (successCallback, failureCallback) ->
        wsService.ws = new WebSocket("ws://localhost:8000/")
        wsService.ws.onopen = successCallback
        wsService.ws.onclose = failureCallback

      handleMessage: (callback) -> wsService.onmessage = callback

    return wsService


angular.module 'starthack'
  .controller 'GameController', ($scope, WebSocket, Pedal) ->

    # Connection stuff
    $scope.status = 'connecting'

    WebSocket.connect ->
      $scope.status = 'connected'
    , ->
      $scope.status = 'disconnected'

    # Command management
    currentAcceleration = 0
    if window.DeviceMotionEvent
      window.ondevicemotion = (e) ->
        currentAcceleration = e.accelerationIncludingGravity.z

    return
