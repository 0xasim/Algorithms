(defun bogo-fib (n)
	"A bogus implementation of the fibonacci function."
	(if (< n 2)
		n
		(+ (bogo-fib (- n 1))
			 (bogo-fib (- n 2)))))

(defun tail-recursive-fib (n)
	"Tail recursiveness substantially reduces execution time"
	(labels ((calc-fib (n a b)
										 (if (= n 0)
											 a
                       (calc-fib (- n 1) b (+ a b)))))
		(calc-fib n 0 1)))

(time (print (tail-recursive-fib 40)))
(time (print (bogo-fib 40)))
