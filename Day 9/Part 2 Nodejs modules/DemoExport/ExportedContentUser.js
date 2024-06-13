//---------Demo 5

var mObject  = require('./ExportedContent');
var result = mObject.Add(10,20);
console.log(result);   

//---------Demo 4

// var Maths = require('./ExportedContent');
// console.log(Maths);

// var mObject = new Maths();
// var result = mObject.Add(10,20);
// console.log(result);    

//---------Demo 3
// var {Sub, Mult} = require('./ExportedContent');

// console.log(Sub);
// var result1 = Sub(10,20);
// console.log(result1);


// console.log(Mult);
// var result2 = Mult(10,20);
// console.log(result2);

// var exportedContent = require('./ExportedContent');
// console.log(exportedContent);




//----------Demo 2
// var exportedContent = require('./ExportedContent');
// console.log(exportedContent);

// var result1 = exportedContent.addition(20,30);
// console.log(result1);

// var result2 = exportedContent.Sub(20,30);
// console.log(result2);

// var result = exportedContent(20,30);
// console.log(result);

//----------Demo 1
// var SayHi = require('./ExportedContent')
// //above statement is as good as:

// // var SayHi =  function ()
// //             {
// //                 console.log("hi");
// //             }

// // console.log(SayHi);

// SayHi();