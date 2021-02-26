const isPrime = num => {
    for(let i = 2, s = Math.sqrt(num); i <= s; i++)
        if(num % i === 0) return false; 
    return num > 1;
}

function formula(n, a, b) {
    return (n*n + a * n + b);
}

function primes(a, b) {
    var count = 0;
    for (var j = 0; j < 1000; j++) {
        if (isPrime(formula(j,a,b))) {
            count++;
        }
        else {
            return count;
        }
    }
    return count;
}

for(var a = 0; a < 1000; a++) {
    for (var b = 0; b < 1000; b++) {
        var temp = [];
        temp.push(primes(a,b));
        temp.push(primes(a,-1*b));
        temp.push(primes(-1*a, b));
        temp.push(primes(-1*a, -1*b));
        for (var i = 0; i < 4; i++) {
            if(temp[i] > max_val) {
                max_val = temp[i];
                var comb=[[1,1],[1,-1],[-1,1],[-1,-1]];
                max_a = comb[i][0] * a;
                max_b = comb[i][1] * b;
            }
        }
    }
}