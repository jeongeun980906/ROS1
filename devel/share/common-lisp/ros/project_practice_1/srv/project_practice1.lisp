; Auto-generated. Do not edit!


(cl:in-package project_practice_1-srv)


;//! \htmlinclude project_practice1-request.msg.html

(cl:defclass <project_practice1-request> (roslisp-msg-protocol:ros-message)
  ((input
    :reader input
    :initarg :input
    :type cl:integer
    :initform 0))
)

(cl:defclass project_practice1-request (<project_practice1-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <project_practice1-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'project_practice1-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name project_practice_1-srv:<project_practice1-request> is deprecated: use project_practice_1-srv:project_practice1-request instead.")))

(cl:ensure-generic-function 'input-val :lambda-list '(m))
(cl:defmethod input-val ((m <project_practice1-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project_practice_1-srv:input-val is deprecated.  Use project_practice_1-srv:input instead.")
  (input m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <project_practice1-request>) ostream)
  "Serializes a message object of type '<project_practice1-request>"
  (cl:let* ((signed (cl:slot-value msg 'input)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <project_practice1-request>) istream)
  "Deserializes a message object of type '<project_practice1-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'input) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<project_practice1-request>)))
  "Returns string type for a service object of type '<project_practice1-request>"
  "project_practice_1/project_practice1Request")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'project_practice1-request)))
  "Returns string type for a service object of type 'project_practice1-request"
  "project_practice_1/project_practice1Request")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<project_practice1-request>)))
  "Returns md5sum for a message object of type '<project_practice1-request>"
  "47de08ae0a6f75933f3d62b872331b10")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'project_practice1-request)))
  "Returns md5sum for a message object of type 'project_practice1-request"
  "47de08ae0a6f75933f3d62b872331b10")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<project_practice1-request>)))
  "Returns full string definition for message of type '<project_practice1-request>"
  (cl:format cl:nil "int64 input~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'project_practice1-request)))
  "Returns full string definition for message of type 'project_practice1-request"
  (cl:format cl:nil "int64 input~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <project_practice1-request>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <project_practice1-request>))
  "Converts a ROS message object to a list"
  (cl:list 'project_practice1-request
    (cl:cons ':input (input msg))
))
;//! \htmlinclude project_practice1-response.msg.html

(cl:defclass <project_practice1-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:boolean
    :initform cl:nil)
   (dir
    :reader dir
    :initarg :dir
    :type cl:integer
    :initform 0))
)

(cl:defclass project_practice1-response (<project_practice1-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <project_practice1-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'project_practice1-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name project_practice_1-srv:<project_practice1-response> is deprecated: use project_practice_1-srv:project_practice1-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <project_practice1-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project_practice_1-srv:result-val is deprecated.  Use project_practice_1-srv:result instead.")
  (result m))

(cl:ensure-generic-function 'dir-val :lambda-list '(m))
(cl:defmethod dir-val ((m <project_practice1-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project_practice_1-srv:dir-val is deprecated.  Use project_practice_1-srv:dir instead.")
  (dir m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <project_practice1-response>) ostream)
  "Serializes a message object of type '<project_practice1-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'result) 1 0)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'dir)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <project_practice1-response>) istream)
  "Deserializes a message object of type '<project_practice1-response>"
    (cl:setf (cl:slot-value msg 'result) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'dir) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<project_practice1-response>)))
  "Returns string type for a service object of type '<project_practice1-response>"
  "project_practice_1/project_practice1Response")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'project_practice1-response)))
  "Returns string type for a service object of type 'project_practice1-response"
  "project_practice_1/project_practice1Response")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<project_practice1-response>)))
  "Returns md5sum for a message object of type '<project_practice1-response>"
  "47de08ae0a6f75933f3d62b872331b10")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'project_practice1-response)))
  "Returns md5sum for a message object of type 'project_practice1-response"
  "47de08ae0a6f75933f3d62b872331b10")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<project_practice1-response>)))
  "Returns full string definition for message of type '<project_practice1-response>"
  (cl:format cl:nil "bool result~%int64 dir~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'project_practice1-response)))
  "Returns full string definition for message of type 'project_practice1-response"
  (cl:format cl:nil "bool result~%int64 dir~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <project_practice1-response>))
  (cl:+ 0
     1
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <project_practice1-response>))
  "Converts a ROS message object to a list"
  (cl:list 'project_practice1-response
    (cl:cons ':result (result msg))
    (cl:cons ':dir (dir msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'project_practice1)))
  'project_practice1-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'project_practice1)))
  'project_practice1-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'project_practice1)))
  "Returns string type for a service object of type '<project_practice1>"
  "project_practice_1/project_practice1")