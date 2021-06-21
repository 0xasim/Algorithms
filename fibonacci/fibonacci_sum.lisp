; Return the sum of fibonacci sequence upto n
(load "~/.quicklisp/setup.lisp")
(ql:quickload "fare-memoization")

(defun fib_rec_basic (n)
  "Naive recursion."
  (if (< n 2)
    n
    (+ (fib_rec_basic (- n 1))
       (fib_rec_basic (- n 2)))))

(defun fib_rec_tailcall (n)
  "Recursion with tailcall optimization."
  (labels ((calc_fib (n a b)
             (if (= n 0)
                 a
                 (calc_fib (- n 1) b (+ a b)))))
    (calc_fib n 0 1)))

(defun fib_rec_memo (n)
  "O(log n). Same as naive recursion but with memoization optimization applied."
  "Actually O(polylog n)"
  (if (< n 2)
    n
    (+ (fib_rec_memo (- n 1))
       (fib_rec_memo (- n 2)))))

(defun fib_loop_bubble (n)
  "O(n). Similar to bubblesort."
  (check-type n fixnum)
  (loop repeat n
      with p = 0 with q = 1
      do (psetq p q
        q (+ p q))
      finally (return p)))



(fare-memoization:memoize 'fib_rec_memo)

(time (print (fib_rec_tailcall 800)))
(time (print (fib_rec_memo 800)))  ; Illegal Harware instruction error for values approx. > 18,800
(time (print (fib_loop_bubble 800)))
;(time (print (fib_rec_basic 40)))

