class WS2Panel_c {
  constructor(ws_url) {
    this.ws_url = ws_url
    this.status = document.getElementById("c-status")
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
    this.upElid(els[0], struct.budget)
    this.upElid(els[1], struct.actual)
    this.upElid(els[2], struct.gap)
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

      this.upElid("c-timestamp", data.timestamp)

      this.upElements([
          "c-09-budget", "c-09-actual", "c-09-gap"
        ], data.month_09)

      this.upElements([
          "c-10-budget", "c-10-actual", "c-10-gap"
        ], data.month_10)
    }
  }
}

document.addEventListener(
  "DOMContentLoaded", function(event) {
    ws_url = "ws://localhost:8765"

    let myPanel = new WS2Panel_c(ws_url)
    myPanel.startWS()
});
