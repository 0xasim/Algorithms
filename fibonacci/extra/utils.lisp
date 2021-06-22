(defun call (f N)
  (print f)
  (print 'Output\:)
  (time (print (funcall f N))))

