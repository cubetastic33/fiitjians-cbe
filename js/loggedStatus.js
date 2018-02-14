firebase.auth().onAuthStateChanged(function(user) {
  hideloader();
  if (user) {
    // User is signed in.
    var nowUser = firebase.auth().currentUser;
    var email = nowUser.email;
    var emailVerified = nowUser.emailVerified;
    var username;
    var profilePic;
    var usersRef = db.ref("users").orderByChild("email").equalTo(email);
    usersRef.once("child_added", function(snapshot) {
      username = snapshot.val().username;
      profilePic = snapshot.val().profilePic;

      if (emailVerified == false) {
        $("#loggedStatus").html("\
          <a href=\"signin.html\" class=\"logout\">Email Not Verified | Sign in</a>\
        ");
        firebase.auth().signOut().then(function() {}).catch(function(error) {});
      } else {
        $('#loggedStatus').html('\
          <a href="profile.html">\
            <img src="'+profilePic+'" id="profilePic" class="circle" alt="profile pic"></img>\
          </a>\
        ');
        $('#signinreqmessage').hide();
        $("#signinreq").show();
      }
    }, function (errorObject) {
      console.log("The read failed: " + errorObject.code);
    });
  } else {
    // No user is signed in.
    if (document.getElementById("loggedStatus").innerHTML == "") {
      $("#loggedStatus").html('\
        <ul class="logout">\
          <li>\
            <a href="signin.html">Sign in</a>\
          </li>\
        </ul>\
      ');
    }
    $('#signinreqmessage').show();
    $("#signinreq").hide();
  }
});
