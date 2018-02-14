function showOldPosts() {
  $('.chips').material_chip();
  $('#memes').empty();
  firebase.auth().onAuthStateChanged(function(user) {
    if (user) {
      var uid = user.uid;
      db.ref('/').on('value', function(snapshot) {
        var posts = snapshot.child('posts').val();
        var postNames = Object.keys(posts);
        for (var i = (postNames.length - 1); i >= 0; i--) {
          var post = posts[postNames[i]];
          if (post.category != 'authorisationReq') {
            $('#memes').append('\
              <div id="post'+postNames[i]+'" class="meme card horizontal hoverable">\
                <div class="card-image">\
                  <img src="'+post.image+'" alt="meme"></img>\
                </div>\
                <div class="card-stacked">\
                  <div class="card-content">\
                    <p><u>'+post.description+'</u></p>\
                    <h5>Category: </h5>'+post.category+'\
                    <h5>Author: </h5>'+post.author+'\
                    <h5>Likes: </h5>'+snapshot.child('posts/'+postNames[i]+'/likes').numChildren()+'<br>\
                    <i id="'+postNames[i]+'" class="material-icons red-text like">thumb_up</i>\
                  </div>\
                </div>\
              </div>\
            ');
          }
          if (post.category == 'authorisationReq' && snapshot.child('users/'+uid+'/authorised').val() == 'yes') {
            $('#memes').append('\
              <div id="post'+postNames[i]+'" class="meme card horizontal hoverable">\
                <div class="card-image">\
                  <img src="'+post.image+'" alt="meme"></img>\
                </div>\
                <div class="card-stacked">\
                  <div class="card-content">\
                    <p><u>'+post.description+'</u></p>\
                    <h5>Category: </h5>'+post.category+'\
                    <h5>Author: </h5>'+post.author+'\
                    <h5>Likes: </h5>'+snapshot.child('posts/'+postNames[i]+'/likes').numChildren()+'<br>\
                    <i id="'+postNames[i]+'" class="material-icons red-text like">thumb_up</i>\
                  </div>\
                </div>\
              </div>\
            ');
          }
        }
        $('.like.red-text').click(function() {
          postName = $(this).attr('id');
          db.ref('posts/'+postName).child('likes').on('value', function(data) {
            existingLikes = parseInt(data.numChildren());
            console.log(postName);
            db.ref('posts/'+postName+'/likes').child(user.uid).set('like');
            $('#'+postName).attr('class', 'material-icons green-text like');
            window.location.href="memes.html";
          });
        });
      });
    } else {
      db.ref('posts').on('value', function(snapshot) {
        var posts = snapshot.val();
        var postNames = Object.keys(posts);
        for (var i = (postNames.length - 1); i >= 0; i--) {
          var post = posts[postNames[i]];
          if (post.category == 'public') {
            $('#memes').append('\
              <div id="post'+postNames[i]+'" class="meme card horizontal hoverable">\
                <div class="card-image">\
                  <img src="'+post.image+'" alt="meme"></img>\
                </div>\
                <div class="card-stacked">\
                  <div class="card-content">\
                    <p><u>'+post.description+'</u></p>\
                    <h5>Category: </h5>'+post.category+'\
                    <h5>Author: </h5>'+post.author+'\
                  </div>\
                </div>\
              </div>\
            ');
          }
        }
      });
    }
  });
}

$('#postBtn').click(function() {
  Materialize.toast('Please wait...');
  //Get values
  var category = $('#category').val();
  var image = document.getElementById('postImage').files[0];
  var description = $('#description').val();
  var tags = $('#tags').material_chip('data');
  var anonymous = document.getElementById('anonymous').checked;
  var newPostName = db.ref('posts').push();
  newPostName.child('category').set(category);
  if (anonymous == true) {
    newPostName.child('author').set('Anonymous');
  } else {
    newPostName.child('author').set(firebase.auth().currentUser.displayName);
  }
  newPostName.child('description').set(description);
  newPostName.child('uid').set(firebase.auth().currentUser.uid);
  tags.forEach(function(item) {
    newPostName.child('tags').push().set(Object.values(item)[0]);
  });
  storage.ref('posts/'+image.name).put(image).then(function() {
    var imageRef = storage.ref('posts/'+image.name);
    imageRef.getDownloadURL().then(function(url) {
      console.log(url);
      newPostName.child('image').set(url);
      window.location.href="memes.html";
    });
  })
});