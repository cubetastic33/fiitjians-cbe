// Initialize Firebase
var config = {
  apiKey: "AIzaSyDb9n4NXrNUfTW0huCJ6tHmY5OOHyUwcWg",
  authDomain: "fiitjians-cbe.firebaseapp.com",
  databaseURL: "https://fiitjians-cbe.firebaseio.com",
  projectId: "fiitjians-cbe",
  storageBucket: "gs://fiitjians-cbe.appspot.com",
  messagingSenderId: "778469198527"
};
firebase.initializeApp(config);

$(document).ready(function() {
  if ($('.button-collapse').length) {
    $('.button-collapse').sideNav();
  }
  if ($('select').length) {
    $('select').material_select();
  }
  if ($('.modal').length) {
    $('.modal').modal();
  }
});
if ($('.datepicker').length) {
  $('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 100,
    max: new Date(),
    today: 'Today',
    clear: 'Clear',
    close: 'Ok',
    closeOnSelect: false
  });
}

$("#signUp").submit(signUpUser);
$("#signIn").submit(signInUser);

var db = firebase.database();
var storage = firebase.storage();
$("#signUp #username").keyup(function() {
  if ($("#username").val() != "") {usernameAvailable($("#username").val())}
});

function usernameAvailable(username) {
  var usernameExists;
  var ref = firebase.database().ref("users").orderByChild("username").equalTo(username);
  $('#username').attr('class', 'valid');
  $('#usernameLabel').attr('data-success', username+' is available.');
  ref.on("child_added", function(snapshot) {
    var usersdata = snapshot.val();
    if (usersdata.username == username) {
      $('#username').attr('class', 'invalid');
      $('#usernameLabel').attr('data-error', usersdata.username+' already exists. Choose a different name!');
      usernameExists = true;
    } else {
      usernameExists = false;
    }
  });
}

function signUpUser(e) {
  e.preventDefault();
  //Get values
  var username = $("#username").val();
  var email = $("#email").val();
  var password = $("#password").val();
  var confPassword = $("#confPassword").val();
  var mobile = $("#mobile").val();
  var dob = $("#dob").val();
  var gender;
  if (($('#usernameLabel').attr('class') != 'invalid') && (password == confPassword) && (gender = $('input[name=gender]:checked', '#signUp').val())) {
    Materialize.toast('Please wait...');
    firebase.auth().createUserWithEmailAndPassword(email, password).catch(function(error) {
      // Handle Errors here.
      var errorCode = error.code;
      var errorMessage = error.message;
      if (errorCode == 'auth/weak-password') {
        $('#password').attr('class', 'invalid');
        $('#passwordLabel').attr('data-error', 'The password is too weak.');
      }
      else {
        Materialize.toast(errorMessage, 10000);
      }
    });

    firebase.auth().onAuthStateChanged(function(user) {
      if (user) {
        var user = firebase.auth().currentUser;
        var uid = user.uid;
        db.ref('users/'+uid).child('authorised').set('no');
        db.ref('users/'+uid).child('dob').set(dob);
        db.ref('users/'+uid).child('email').set(email);
        db.ref('users/'+uid).child('gender').set(gender);
        db.ref('users/'+uid).child('mobile').set(mobile);
        db.ref('users/'+uid).child('profilePic').set('/images/defaultProfilePic.png');
        db.ref('users/'+uid).child('username').set(username);
        user.displayName = username;
        user.sendEmailVerification().then(function() {
          // Email sent.
          alert("Verification email has been sent.");
          window.location.href="index.html";
        }).catch(function(error) {
          // An error happened.
          Materialize.toast(errorMessage, 10000);
        });
      }
    });
  } else if (password != confPassword) {
    $('#confPassword').attr('class', 'invalid');
    $('#confPasswordLabel').attr('data-error', 'The two passwords don\'t match!');
  } else if ($('#username').attr('class') == 'valid') {
    Materialize.toast('Please select your gender!');
  }
}

function signInUser(e) {
  e.preventDefault();
  //Get values
  var username = $("#username").val();
  var password = $("#password").val();

  var usersRef = db.ref('users').orderByChild('username').equalTo(username);
  usersRef.once("child_added", function(snapshot) {
    email = snapshot.val().email;
    firebase.auth().signInWithEmailAndPassword(email, password).catch(function(error) {
      // Handle Errors here.
      var errorCode = error.code;
      var errorMessage = error.message;
      Materialize.toast(errorMessage);
    });
    firebase.auth().onAuthStateChanged(function(user) {
      if (user) {
        // User is signed in.
        window.location.href="index.html";
      } else {
        // No user is signed in.
      }
    });
  }, function (errorObject) {
    console.log("The read failed: " + errorObject.code);
  });
}

$('#forgotPassword').click(function() {
  firebase.auth().sendPasswordResetEmail(prompt('Enter your email address')).then(function() {
    console.log('Sent password reset email.');
  }).catch(function(error) {
    console.log('Error: ', error);
  });
});

function signOutUser() {
  firebase.auth().signOut().then(function() {}).catch(function(error) {console.log(error);});
}
