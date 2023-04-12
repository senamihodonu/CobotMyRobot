// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from action_interfaces:action/SetAngle.idl
// generated code does not contain a copyright notice

#ifndef ACTION_INTERFACES__ACTION__DETAIL__SET_ANGLE__BUILDER_HPP_
#define ACTION_INTERFACES__ACTION__DETAIL__SET_ANGLE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "action_interfaces/action/detail/set_angle__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace action_interfaces
{

namespace action
{

namespace builder
{

class Init_SetAngle_Goal_speed
{
public:
  explicit Init_SetAngle_Goal_speed(::action_interfaces::action::SetAngle_Goal & msg)
  : msg_(msg)
  {}
  ::action_interfaces::action::SetAngle_Goal speed(::action_interfaces::action::SetAngle_Goal::_speed_type arg)
  {
    msg_.speed = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_interfaces::action::SetAngle_Goal msg_;
};

class Init_SetAngle_Goal_angles
{
public:
  Init_SetAngle_Goal_angles()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SetAngle_Goal_speed angles(::action_interfaces::action::SetAngle_Goal::_angles_type arg)
  {
    msg_.angles = std::move(arg);
    return Init_SetAngle_Goal_speed(msg_);
  }

private:
  ::action_interfaces::action::SetAngle_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_interfaces::action::SetAngle_Goal>()
{
  return action_interfaces::action::builder::Init_SetAngle_Goal_angles();
}

}  // namespace action_interfaces


namespace action_interfaces
{

namespace action
{

namespace builder
{

class Init_SetAngle_Result_end_angles
{
public:
  Init_SetAngle_Result_end_angles()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::action_interfaces::action::SetAngle_Result end_angles(::action_interfaces::action::SetAngle_Result::_end_angles_type arg)
  {
    msg_.end_angles = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_interfaces::action::SetAngle_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_interfaces::action::SetAngle_Result>()
{
  return action_interfaces::action::builder::Init_SetAngle_Result_end_angles();
}

}  // namespace action_interfaces


namespace action_interfaces
{

namespace action
{


}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_interfaces::action::SetAngle_Feedback>()
{
  return ::action_interfaces::action::SetAngle_Feedback(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace action_interfaces


namespace action_interfaces
{

namespace action
{

namespace builder
{

class Init_SetAngle_SendGoal_Request_goal
{
public:
  explicit Init_SetAngle_SendGoal_Request_goal(::action_interfaces::action::SetAngle_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::action_interfaces::action::SetAngle_SendGoal_Request goal(::action_interfaces::action::SetAngle_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_interfaces::action::SetAngle_SendGoal_Request msg_;
};

class Init_SetAngle_SendGoal_Request_goal_id
{
public:
  Init_SetAngle_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SetAngle_SendGoal_Request_goal goal_id(::action_interfaces::action::SetAngle_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_SetAngle_SendGoal_Request_goal(msg_);
  }

private:
  ::action_interfaces::action::SetAngle_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_interfaces::action::SetAngle_SendGoal_Request>()
{
  return action_interfaces::action::builder::Init_SetAngle_SendGoal_Request_goal_id();
}

}  // namespace action_interfaces


namespace action_interfaces
{

namespace action
{

namespace builder
{

class Init_SetAngle_SendGoal_Response_stamp
{
public:
  explicit Init_SetAngle_SendGoal_Response_stamp(::action_interfaces::action::SetAngle_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::action_interfaces::action::SetAngle_SendGoal_Response stamp(::action_interfaces::action::SetAngle_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_interfaces::action::SetAngle_SendGoal_Response msg_;
};

class Init_SetAngle_SendGoal_Response_accepted
{
public:
  Init_SetAngle_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SetAngle_SendGoal_Response_stamp accepted(::action_interfaces::action::SetAngle_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_SetAngle_SendGoal_Response_stamp(msg_);
  }

private:
  ::action_interfaces::action::SetAngle_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_interfaces::action::SetAngle_SendGoal_Response>()
{
  return action_interfaces::action::builder::Init_SetAngle_SendGoal_Response_accepted();
}

}  // namespace action_interfaces


namespace action_interfaces
{

namespace action
{

namespace builder
{

class Init_SetAngle_GetResult_Request_goal_id
{
public:
  Init_SetAngle_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::action_interfaces::action::SetAngle_GetResult_Request goal_id(::action_interfaces::action::SetAngle_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_interfaces::action::SetAngle_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_interfaces::action::SetAngle_GetResult_Request>()
{
  return action_interfaces::action::builder::Init_SetAngle_GetResult_Request_goal_id();
}

}  // namespace action_interfaces


namespace action_interfaces
{

namespace action
{

namespace builder
{

class Init_SetAngle_GetResult_Response_result
{
public:
  explicit Init_SetAngle_GetResult_Response_result(::action_interfaces::action::SetAngle_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::action_interfaces::action::SetAngle_GetResult_Response result(::action_interfaces::action::SetAngle_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_interfaces::action::SetAngle_GetResult_Response msg_;
};

class Init_SetAngle_GetResult_Response_status
{
public:
  Init_SetAngle_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SetAngle_GetResult_Response_result status(::action_interfaces::action::SetAngle_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_SetAngle_GetResult_Response_result(msg_);
  }

private:
  ::action_interfaces::action::SetAngle_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_interfaces::action::SetAngle_GetResult_Response>()
{
  return action_interfaces::action::builder::Init_SetAngle_GetResult_Response_status();
}

}  // namespace action_interfaces


namespace action_interfaces
{

namespace action
{

namespace builder
{

class Init_SetAngle_FeedbackMessage_feedback
{
public:
  explicit Init_SetAngle_FeedbackMessage_feedback(::action_interfaces::action::SetAngle_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::action_interfaces::action::SetAngle_FeedbackMessage feedback(::action_interfaces::action::SetAngle_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_interfaces::action::SetAngle_FeedbackMessage msg_;
};

class Init_SetAngle_FeedbackMessage_goal_id
{
public:
  Init_SetAngle_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SetAngle_FeedbackMessage_feedback goal_id(::action_interfaces::action::SetAngle_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_SetAngle_FeedbackMessage_feedback(msg_);
  }

private:
  ::action_interfaces::action::SetAngle_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_interfaces::action::SetAngle_FeedbackMessage>()
{
  return action_interfaces::action::builder::Init_SetAngle_FeedbackMessage_goal_id();
}

}  // namespace action_interfaces

#endif  // ACTION_INTERFACES__ACTION__DETAIL__SET_ANGLE__BUILDER_HPP_
