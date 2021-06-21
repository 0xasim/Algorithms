; Return the sum of fibonacci sequence upto n
(declaim (optimize (speed 0) (safety 3) (debug 3)))

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
  ;(memoize (fn 
  )


(time (print (fib_rec_tailcall 40)))
(time (print (fib_rec_basic 40)))

