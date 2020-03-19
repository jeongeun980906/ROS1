// Generated by gencpp from file open_manipulator_msgs/JointPose.msg
// DO NOT EDIT!


#ifndef OPEN_MANIPULATOR_MSGS_MESSAGE_JOINTPOSE_H
#define OPEN_MANIPULATOR_MSGS_MESSAGE_JOINTPOSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace open_manipulator_msgs
{
template <class ContainerAllocator>
struct JointPose_
{
  typedef JointPose_<ContainerAllocator> Type;

  JointPose_()
    : joint_name()
    , position()
    , move_time(0.0)  {
    }
  JointPose_(const ContainerAllocator& _alloc)
    : joint_name(_alloc)
    , position(_alloc)
    , move_time(0.0)  {
  (void)_alloc;
    }



   typedef std::vector<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > , typename ContainerAllocator::template rebind<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::other >  _joint_name_type;
  _joint_name_type joint_name;

   typedef std::vector<double, typename ContainerAllocator::template rebind<double>::other >  _position_type;
  _position_type position;

   typedef double _move_time_type;
  _move_time_type move_time;





  typedef boost::shared_ptr< ::open_manipulator_msgs::JointPose_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::open_manipulator_msgs::JointPose_<ContainerAllocator> const> ConstPtr;

}; // struct JointPose_

typedef ::open_manipulator_msgs::JointPose_<std::allocator<void> > JointPose;

typedef boost::shared_ptr< ::open_manipulator_msgs::JointPose > JointPosePtr;
typedef boost::shared_ptr< ::open_manipulator_msgs::JointPose const> JointPoseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::open_manipulator_msgs::JointPose_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::open_manipulator_msgs::JointPose_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace open_manipulator_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'geometry_msgs': ['/opt/ros/melodic/share/geometry_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg'], 'open_manipulator_msgs': ['/home/jhmbabo/catkin_ws/src/turtlebot3/open_manipulator/open_manipulator_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::open_manipulator_msgs::JointPose_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::open_manipulator_msgs::JointPose_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::open_manipulator_msgs::JointPose_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::open_manipulator_msgs::JointPose_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::open_manipulator_msgs::JointPose_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::open_manipulator_msgs::JointPose_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::open_manipulator_msgs::JointPose_<ContainerAllocator> >
{
  static const char* value()
  {
    return "217de178e1835082dfab23527f9a9de9";
  }

  static const char* value(const ::open_manipulator_msgs::JointPose_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x217de178e1835082ULL;
  static const uint64_t static_value2 = 0xdfab23527f9a9de9ULL;
};

template<class ContainerAllocator>
struct DataType< ::open_manipulator_msgs::JointPose_<ContainerAllocator> >
{
  static const char* value()
  {
    return "open_manipulator_msgs/JointPose";
  }

  static const char* value(const ::open_manipulator_msgs::JointPose_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::open_manipulator_msgs::JointPose_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string[]   joint_name\n"
"float64[]  position\n"
"float64    move_time\n"
;
  }

  static const char* value(const ::open_manipulator_msgs::JointPose_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::open_manipulator_msgs::JointPose_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.joint_name);
      stream.next(m.position);
      stream.next(m.move_time);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct JointPose_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::open_manipulator_msgs::JointPose_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::open_manipulator_msgs::JointPose_<ContainerAllocator>& v)
  {
    s << indent << "joint_name[]" << std::endl;
    for (size_t i = 0; i < v.joint_name.size(); ++i)
    {
      s << indent << "  joint_name[" << i << "]: ";
      Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.joint_name[i]);
    }
    s << indent << "position[]" << std::endl;
    for (size_t i = 0; i < v.position.size(); ++i)
    {
      s << indent << "  position[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.position[i]);
    }
    s << indent << "move_time: ";
    Printer<double>::stream(s, indent + "  ", v.move_time);
  }
};

} // namespace message_operations
} // namespace ros

#endif // OPEN_MANIPULATOR_MSGS_MESSAGE_JOINTPOSE_H
