$(document).ready(function(){
  url = window.location.href;
  var PROPS = ['name','grade','sex','motivation','behavior','participation','postivies','negatives'];
  // var submitDict = {};
  // for(var i = 0; i < PROPS.length; i++){
  //   submitDict[PROPS[i]] = [];
  // }

  $("#submit").click(function(){
    classList = [];
    var numStudents = Number(url.substring(32));
    for(var i = 0; i < numStudents; i++){
      //var propClass = "." + PROPS[i];
      var studentClass = ".student" + i;
      inputs = $(studentClass);
      student = {};
      for(var i = 0; i < PROPS.lenght; i ++){
        student[PROPS[i]] = inputs[i].value;
        classList.push(student);
      }
    }
    console.log(classList);
  })
});