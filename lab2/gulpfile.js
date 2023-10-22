var gulp = require('gulp');


// функция базового таска для gulp 
function defaultTask(callback) {
    console.log("hello world! it's gulp!");
    callback();
}


gulp.task("count", function(callback) {
    // пятый аргумент это будет аргумент после --num
    var num = process.argv[4] ? process.argv[4] : 0;
    if (num <= 0) {
        console.log("Nothing to count");
    } else {
        for (var i = 1; i <= num; i++) console.log(i);
    }
    callback();
})

// экспортируем таск как стандартный для gulp
exports.default = defaultTask
