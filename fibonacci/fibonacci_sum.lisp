; Return the sum of fibonacci sequence upto n
(load "~/.quicklisp/setup.lisp")
(ql:quickload "fare-memoization")

(defun fib_rec_basic (n)
  "naive recursion"
  (if (< n 2)
    n
    (+ (fib_rec_basic (- n 1))
       (fib_rec_basic (- n 2)))))

(defun fib_rec_tailcall (n)
  "tailcall Optimized recursion"
  (labels ((calc_fib (n a b)
             (if (= n 0)
                 a
                 (calc_fib (- n 1) b (+ a b)))))
    (calc_fib n 0 1)))

(defun fib_rec_memo (n)
  "Memoization optimized recursion"
  (if (< n 2)
    n
    (+ (fib_rec_memo (- n 1))
       (fib_rec_memo (- n 2)))))

(fare-memoization:memoize 'fib_rec_memo)

(time (print (fib_rec_tailcall 40)))
(time (print (fib_rec_memo 40)))
(time (print (fib_rec_basic 40)))

