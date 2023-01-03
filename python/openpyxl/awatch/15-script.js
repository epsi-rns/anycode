document.addEventListener(
  "DOMContentLoaded", function(event) {
     const websocket = new WebSocket("ws://localhost:8765");
     const value_a1 = document.getElementById("value-a1");
     const value_a2 = document.getElementById("value-a2");
     const value_a3 = document.getElementById("value-a3");

     websocket.onmessage = function(event) {
       const data = JSON.parse(event.data); 
       value_a1.innerHTML = data.val1;
       value_a2.innerHTML = data.val2;
       value_a3.innerHTML = data.val3;
     }
});
