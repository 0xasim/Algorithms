(defun factorial (N)
  "Compute factorial of N."
  (if (= N 1)
      1
    (* N (factorial (- N 1)))))
