; Return the sum of fibonacci sequence upto n

(defun basic-recursive-fib (n)
  "basic recursion"
  (if (< n 2)
    n
    (+ (basic-recursive-fib (- n 1))
       (basic-recursive-fib (- n 2)))))

(defun tail-recursive-fib (n)
  "tailcall Optimized recursion"
  (labels ((calc-fib (n a b)
             (if (= n 0)
                 a
                 (calc-fib (- n 1) b (+ a b)))))
    (calc-fib n 0 1)))

(defun memo-fib (n)

(time (print (tail-recursive-fib 40)))
(time (print (basic-recursive-fib 40)))
