(function() {
  'use strict';

  document.addEventListener('DOMNodeInserted', event => {
    let connectButton = document.querySelector("#connect");
    


    function connect() {
      port.connect().then(() => {
        
        connectButton.textContent = 'DISCONNECT';

        port.onReceive = data => {
          let textDecoder = new TextDecoder();
          console.log(textDecoder.decode(data));
        }
        port.onReceiveError = error => {
          console.error(error);
        };
      }, error => {
        
      });
    }
    try {
    connectButton.addEventListener('click', function() {
      if (port) {
        port.disconnect();
        connectButton.textContent = 'CONNECT ARDUINO';
        
        port = null;
      } else {
        serial.requestPort().then(selectedPort => {
          port = selectedPort;
          connect();
        }).catch(error => {
          
        });
      }
    });
      
    }
    catch (e) {
      
      console.log("p5 sketch not loaded yet: ", e);
    }

//     serial.getPorts().then(ports => {
//       if (ports.length == 0) {
        
//       } else {
        
//         port = ports[0];
//         connect();
//       }
//     });
  });
})();


// From https://github.com/webusb/arduino/blob/gh-pages/demos/serial.js
var serial = {};

(function() {
  'use strict';

  serial.getPorts = function() {
    return navigator.usb.getDevices().then(devices => {
      console.log(devices);
      return devices.map(device => new serial.Port(device));
    });
  };

  serial.requestPort = function() {
    const filters = [
      { 'vendorId': 0x2341, 'productId': 0x8036 },
      { 'vendorId': 0x2341, 'productId': 0x8037 },
      { 'vendorId': 0x2341, 'productId': 0x804d },
      { 'vendorId': 0x2341, 'productId': 0x804e },
      { 'vendorId': 0x2341, 'productId': 0x804f },
      { 'vendorId': 0x2341, 'productId': 0x8050 },
      { 'vendorId': 0x0D28, 'productId': 0x0204 },
    ];
    return navigator.usb.requestDevice({ 'filters': filters }).then(
      device => new serial.Port(device)
    );
  }

  serial.Port = function(device) {
    this.device_ = device;
  };

  serial.Port.prototype.connect = function() {
    let readLoop = () => {
      this.device_.transferIn(5, 64).then(result => {
        this.onReceive(result.data);
        readLoop();
      }, error => {
        this.onReceiveError(error);
      });
    };

    return this.device_.open()
        .then(() => {
          if (this.device_.configuration === null) {
            return this.device_.selectConfiguration(1);
          }
        })
        .then(() => this.device_.claimInterface(2))
        .then(() => this.device_.selectAlternateInterface(2, 0))
        .then(() => this.device_.controlTransferOut({
            'requestType': 'class',
            'recipient': 'interface',
            'request': 0x22,
            'value': 0x01,
            'index': 0x02}))
        .then(() => {
          readLoop();
        });
  };

  serial.Port.prototype.disconnect = function() {
    return this.device_.controlTransferOut({
            'requestType': 'class',
            'recipient': 'interface',
            'request': 0x22,
            'value': 0x00,
            'index': 0x02})
        .then(() => this.device_.close());
  };

  serial.Port.prototype.send = function(data) {
    return this.device_.transferOut(4, data);
  };
})();

