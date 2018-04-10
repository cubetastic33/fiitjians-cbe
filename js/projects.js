$('#switchInputMethod').click(switchInputMethod);

function switchInputMethod() {
  if ($('#instructions').html().toString().includes('Choose two') == true) {
    $('#instructions').html('\
      Enter two +<sup>ve</sup> integers &le; 9223372036854775807 (around 64 bytes, 2<sup>63</sup> - 1, the -1 because of 0) in the input fields below, or <span id="switchInputMethod" class="blue-text">change the input method</span>.\
    ');
    $('#switchInputMethod').click(switchInputMethod);
    $('#inputMethod').html('\
      <div class="input-field col s6">\
        <input type="number" id="number1" value="1467654368">\
      </div>\
      <div class="input-field col s6">\
        <input type="number" id="number2" value="45351972">\
      </div>\
    ');
  } else {
    $('#instructions').html('\
      Choose two +<sup>ve</sup> integers using the number selectors below, or <span id="switchInputMethod" class="blue-text">change the input method</span>.\
    ');
    $('#switchInputMethod').click(switchInputMethod);
    $('#inputMethod').html('\
      <p class="range-field col s6">\
        <input type="range" id="number1" min="0" max="10000"/>\
      </p>\
      <p class="range-field col s6">\
        <input type="range" id="number2" min="0" max="10000"/>\
      </p>\
    ');
  }
}

function calculate() {
  Materialize.toast('Please wait! It takes some time to calculate, because this free server only provides 500MB RAM', 3000)
  $.ajax({
    type: 'GET',
    url: '/calculate',
    data: {
      number1: $('#number1').val(),
      number2: $('#number2').val()
    },
    success: function(result) {
      console.log(result);
      $('#showQuestions').html('Your numbers: ' + $('#number1').val() + ', ' + $('#number2').val());
      $('#hcf').html('<b>HCF: </b>' + result.hcf);
      $('#lcm').html('<b>LCM: </b>' + result.lcm);
      console.log(result.steps);
      $('#steps').html('<b>Steps taken to find HCF: </b>');
      for (var i = 0; i < result.steps.length/2; i++) {
        $('#steps').append('<br>' + result.steps[i]);
      }
    }
  });
}

function findFactors() {
  Materialize.toast('This is likely to take a lot of time, but everything is done in the server, and not on your device', 3000);
  $.ajax({
    type: 'GET',
    url: '/find_factors',
    data: {
      number1: $('#number1').val(),
      number2: $('#number2').val()
    },
    success: function(result) {
      console.log(result);
      $('#showQuestions').html('Your numbers: ' + $('#number1').val() + ', ' + $('#number2').val());
      $('#factors').html('<b>Factors: </b>' + result.factors);
    }
  });
}
