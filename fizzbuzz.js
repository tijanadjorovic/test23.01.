for (var i = 1; i <= 100; i++) {
    var fizz = i % 3 == 0,
        buzz = i % 5 == 0;
    console.log(fizz ? buzz ? "FizzBuzz" : "Fizz" : buzz ? "Buzz" : i);
}