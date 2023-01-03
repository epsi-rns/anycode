document.addEventListener(
  "DOMContentLoaded", function(event) {
    const value1 = document.getElementById("value1");
    const value2 = document.getElementById("value2");
    const value3 = document.getElementById("value3");

    function start(){
      const websocket = new WebSocket("ws://localhost:8765");

      websocket.onmessage = function(event) {
        const data = JSON.parse(event.data); 
        value1.innerHTML = data.val1;
        value2.innerHTML = data.val2;
        value3.innerHTML = data.val3;
      }

      websocket.onclose = function(){
        // Try to reconnect in 5 seconds
        setTimeout(function(){start()}, 5000);
      };
    }

    start();
});
