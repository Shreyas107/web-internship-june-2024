//----------------------------------Async Read

var fs = require('fs');

console.log("Hi........");

fs.readdir("c:\\DMC\\",(error, result)=>{
            // console.log(error);
            // console.log("-------")
            // console.log(result);

            if(error==null)
            {
                
                for(i=0;i<result.length; i++)
                {
                    console.log(result[i]);
                }
            }
        });

console.log("Bye........");



//-------------------------------------------

//----------------------------------Sync Read

// var fs = require('fs');
// // console.log(fs);

// console.log("Hi........");

// var directoryContents = fs.readdirSync("c:\\DMC\\");

// for(i=0;i<directoryContents.length; i++)
// {
//     console.log(directoryContents[i]);
// }


// console.log("Bye........");



//-------------------------------------------


//var os = require('os')
// console.log(os);
// console.log(os.freemem());
// console.log(os.arch())