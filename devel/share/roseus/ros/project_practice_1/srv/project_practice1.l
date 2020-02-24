;; Auto-generated. Do not edit!


(when (boundp 'project_practice_1::project_practice1)
  (if (not (find-package "PROJECT_PRACTICE_1"))
    (make-package "PROJECT_PRACTICE_1"))
  (shadow 'project_practice1 (find-package "PROJECT_PRACTICE_1")))
(unless (find-package "PROJECT_PRACTICE_1::PROJECT_PRACTICE1")
  (make-package "PROJECT_PRACTICE_1::PROJECT_PRACTICE1"))
(unless (find-package "PROJECT_PRACTICE_1::PROJECT_PRACTICE1REQUEST")
  (make-package "PROJECT_PRACTICE_1::PROJECT_PRACTICE1REQUEST"))
(unless (find-package "PROJECT_PRACTICE_1::PROJECT_PRACTICE1RESPONSE")
  (make-package "PROJECT_PRACTICE_1::PROJECT_PRACTICE1RESPONSE"))

(in-package "ROS")





(defclass project_practice_1::project_practice1Request
  :super ros::object
  :slots (_input ))

(defmethod project_practice_1::project_practice1Request
  (:init
   (&key
    ((:input __input) 0)
    )
   (send-super :init)
   (setq _input (round __input))
   self)
  (:input
   (&optional __input)
   (if __input (setq _input __input)) _input)
  (:serialization-length
   ()
   (+
    ;; int64 _input
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _input
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _input (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _input) (= (length (_input . bv)) 2)) ;; bignum
              (write-long (ash (elt (_input . bv) 0) 0) s)
              (write-long (ash (elt (_input . bv) 1) -1) s))
             ((and (class _input) (= (length (_input . bv)) 1)) ;; big1
              (write-long (elt (_input . bv) 0) s)
              (write-long (if (>= _input 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _input s)(write-long (if (>= _input 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _input
#+(or :alpha :irix6 :x86_64)
      (setf _input (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _input (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(defclass project_practice_1::project_practice1Response
  :super ros::object
  :slots (_result _x _y ))

(defmethod project_practice_1::project_practice1Response
  (:init
   (&key
    ((:result __result) nil)
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    )
   (send-super :init)
   (setq _result __result)
   (setq _x (float __x))
   (setq _y (float __y))
   self)
  (:result
   (&optional __result)
   (if __result (setq _result __result)) _result)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:serialization-length
   ()
   (+
    ;; bool _result
    1
    ;; float64 _x
    8
    ;; float64 _y
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _result
       (if _result (write-byte -1 s) (write-byte 0 s))
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _result
     (setq _result (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass project_practice_1::project_practice1
  :super ros::object
  :slots ())

(setf (get project_practice_1::project_practice1 :md5sum-) "7525b31207ccda06e56279e244da6731")
(setf (get project_practice_1::project_practice1 :datatype-) "project_practice_1/project_practice1")
(setf (get project_practice_1::project_practice1 :request) project_practice_1::project_practice1Request)
(setf (get project_practice_1::project_practice1 :response) project_practice_1::project_practice1Response)

(defmethod project_practice_1::project_practice1Request
  (:response () (instance project_practice_1::project_practice1Response :init)))

(setf (get project_practice_1::project_practice1Request :md5sum-) "7525b31207ccda06e56279e244da6731")
(setf (get project_practice_1::project_practice1Request :datatype-) "project_practice_1/project_practice1Request")
(setf (get project_practice_1::project_practice1Request :definition-)
      "int64 input
---
bool result
float64 x
float64 y

")

(setf (get project_practice_1::project_practice1Response :md5sum-) "7525b31207ccda06e56279e244da6731")
(setf (get project_practice_1::project_practice1Response :datatype-) "project_practice_1/project_practice1Response")
(setf (get project_practice_1::project_practice1Response :definition-)
      "int64 input
---
bool result
float64 x
float64 y

")



(provide :project_practice_1/project_practice1 "7525b31207ccda06e56279e244da6731")


