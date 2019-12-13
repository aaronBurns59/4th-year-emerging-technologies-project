    
    // Adpated from: https://www.html5canvastutorials.com/labs/html5-canvas-paint-application/
    
    //Drawing on the canvas =============================================================
    // getting the canvas from the body 
    var canvas = document.getElementById('canvasID');
    // creating a var to draw the digits
    var ctx = canvas.getContext('2d');
    
    // getting the id of the div the canvas is contained in
    var painting = document.getElementById('canvasDiv');
    var paint_style = getComputedStyle(painting);

    // get the width and height of the canvas from the canvas element in the html tag
    canvas.width = parseInt(paint_style.getPropertyValue('width'));
    canvas.height = parseInt(paint_style.getPropertyValue('height'));
    
    // set the params of the mouse to 0, 0
    var mouse = {x: 0, y: 0};

    // determine and correct to offset of the mouse on the canvas
    canvas.addEventListener('mousemove',  function(e){
      mouse.x = e.pageX - this.offsetLeft;
      mouse.y = e.pageY - this.offsetTop;
    }, false);

    // Changing the properties of the ctx
    ctx.lineWidth = 5;
    ctx.lineJoin = 'round';
    ctx.linCap = 'round';
    ctx.strokeStyle = '#FFFFFF';

    canvas.addEventListener('mousedown',function(e){
      ctx.beginPath();
      ctx.moveTo(mouse.x, mouse.y);
      canvas.addEventListener('mousemove', onPaint, false);
    }, false);

    canvas.addEventListener('mouseup', function(e){
      canvas.removeEventListener('mousemove', onPaint, false);
    }, false);

    var onPaint = function() {
      ctx.lineTo(mouse.x, mouse.y);
      ctx.stroke();
    };

    // JQuery Methods ===========================================================
    // Reset the canvas
    $('#resetBtn').click(function(){
      var canvas = document.getElementById('canvasID');
      var ctx = canvas.getContext('2d');
      ctx.clearRect(0, 0,  canvas.width, canvas.height);
    });
    
    // Save the Canvas
    $('#saveBtn').click(function(){
    var canvas = document.getElementById("canvasID");
    var dataURL=canvas.toDataURL();
    console.log(dataURL);
    $.ajax({
      type: 'POST',
      url: '/predictDigit',
      data: {
        imgBase64: dataURL
      }
    }).done(function(result){
      console.log('SENT' + result);
      $("#result").empty().append(result);
    });
  });