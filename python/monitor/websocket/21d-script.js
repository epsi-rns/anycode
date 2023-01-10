class WS2Panel_d {
  constructor(ws_url) {
    this.ws_url = ws_url
    this.status = document.getElementById("d-status")
  }

  // Update Element ID
  upElid(elementID, value) {
    // Set value at placeholder
    const el = document.getElementById(elementID)
    el.innerHTML= value
  }

  // Update Element IDs
  upElements(els, struct) {
    // Map all row value into its placeholders
    this.upElid(els[0], struct.target)
    this.upElid(els[1], struct.actual)
    this.upElid(els[2], struct.miss)
    this.upElid(els[3], struct.remain)
  }

  // Loop Entry Point
  startWS() {
    const websocket = new WebSocket(this.ws_url)

    websocket.onopen = () => {
      this.status.innerHTML = "Opened"
      websocket.send("Hello There.");
    }

    websocket.onclose = () => {
      this.status.innerHTML = "Closed"
      // Try to reconnect in 5 seconds
      setTimeout(() => {
        this.startWS()
      }, 5000)
    };

    websocket.onmessage = (event) => {
      const data = JSON.parse(event.data)

      this.upElid("d-timestamp", data.timestamp)

      this.upElements([
          "d-09-target", "d-09-actual",
          "d-09-miss",   "d-09-remain"
        ], data.month_09)

      this.upElements([
          "d-10-target", "d-10-actual",
          "d-10-miss",   "d-10-remain"
        ], data.month_10)

      this.upElements([
          "d-11-target", "d-11-actual",
          "d-11-miss",   "d-11-remain"
        ], data.month_11)

      this.upElements([
          "d-total-target", "d-total-actual",
          "d-total-miss",   "d-total-remain"
        ], data.total)
    }
  }
}

document.addEventListener(
  "DOMContentLoaded", function(event) {
    ws_url = "ws://localhost:8767"

    let myPanel = new WS2Panel_d(ws_url)
    myPanel.startWS()
});
