document.addEventListener(
  "DOMContentLoaded", function(event) {

    // Get all value placholder
    const time_a   = document.getElementById("time-a");
    const status_a = document.getElementById("status-a");
    const value_a1 = document.getElementById("value-a1");
    const value_a2 = document.getElementById("value-a2");
    const value_a3 = document.getElementById("value-a3");

    // Loop Entry Point
    function startWS(){
      const websocket = new WebSocket("ws://localhost:8765");

      websocket.onopen = function () {
        status_a.innerHTML = "Opened";
        websocket.send("Hello There.");
      };

      websocket.onmessage = function(event) {
        const data = JSON.parse(event.data); 

        time_a.innerHTML   = data.time;
        value_a1.innerHTML = data.val1;
        value_a2.innerHTML = data.val2;
        value_a3.innerHTML = data.val3;
      }

      websocket.onclose = function(){
        status_a.innerHTML = "Closed";
        // Try to reconnect in 5 seconds
        setTimeout(function(){start()}, 5000);
      };
    }

    startWS();
});
