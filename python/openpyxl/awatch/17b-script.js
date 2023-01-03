document.addEventListener(
  "DOMContentLoaded", function(event) {

    // Get all value placholder
    const time_b   = document.getElementById("time-b");
    const status_b = document.getElementById("status-b");
    const value_b1 = document.getElementById("value-b1");
    const value_b2 = document.getElementById("value-b2");
    const value_b3 = document.getElementById("value-b3");

    // Loop Entry Point
    function startWS(){
      const websocket = new WebSocket("ws://localhost:8767");

      websocket.onopen = function () {
        status_b.innerHTML = "Opened";
        websocket.send("Hello There.");
      };

      websocket.onmessage = function(event) {
        const data = JSON.parse(event.data); 

        time_b.innerHTML   = data.time;
        value_b1.innerHTML = data.val1;
        value_b2.innerHTML = data.val2;
        value_b3.innerHTML = data.val3;
      }

      websocket.onclose = function(){
        status_b.innerHTML = "Closed";
        // Try to reconnect in 5 seconds
        setTimeout(function(){start()}, 5000);
      };
    }

    startWS();
});
