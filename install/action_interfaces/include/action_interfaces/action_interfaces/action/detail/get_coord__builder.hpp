// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from action_interfaces:action/GetCoord.idl
// generated code does not contain a copyright notice

#ifndef ACTION_INTERFACES__ACTION__DETAIL__GET_COORD__BUILDER_HPP_
#define ACTION_INTERFACES__ACTION__DETAIL__GET_COORD__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "action_interfaces/action/detail/get_coord__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace action_interfaces
{

namespace action
{


}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_interfaces::action::GetCoord_Goal>()
{
  return ::action_interfaces::action::GetCoord_Goal(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace action_interfaces


namespace action_interfaces
{

namespace action
{

namespace builder
{

class Init_GetCoord_Result_end_coords
{
public:
  Init_GetCoord_Result_end_coords()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::action_interfaces::action::GetCoord_Result end_coords(::action_interfaces::action::GetCoord_Result::_end_coords_type arg)
  {
    msg_.end_coords = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_interfaces::action::GetCoord_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_interfaces::action::GetCoord_Result>()
{
  return action_interfaces::action::builder::Init_GetCoord_Result_end_coords();
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
auto build<::action_interfaces::action::GetCoord_Feedback>()
{
  return ::action_interfaces::action::GetCoord_Feedback(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace action_interfaces


namespace action_interfaces
{

namespace action
{

namespace builder
{

class Init_GetCoord_SendGoal_Request_goal
{
public:
  explicit Init_GetCoord_SendGoal_Request_goal(::action_interfaces::action::GetCoord_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::action_interfaces::action::GetCoord_SendGoal_Request goal(::action_interfaces::action::GetCoord_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_interfaces::action::GetCoord_SendGoal_Request msg_;
};

class Init_GetCoord_SendGoal_Request_goal_id
{
public:
  Init_GetCoord_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GetCoord_SendGoal_Request_goal goal_id(::action_interfaces::action::GetCoord_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_GetCoord_SendGoal_Request_goal(msg_);
  }

private:
  ::action_interfaces::action::GetCoord_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_interfaces::action::GetCoord_SendGoal_Request>()
{
  return action_interfaces::action::builder::Init_GetCoord_SendGoal_Request_goal_id();
}

}  // namespace action_interfaces


namespace action_interfaces
{

namespace action
{

namespace builder
{

class Init_GetCoord_SendGoal_Response_stamp
{
public:
  explicit Init_GetCoord_SendGoal_Response_stamp(::action_interfaces::action::GetCoord_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::action_interfaces::action::GetCoord_SendGoal_Response stamp(::action_interfaces::action::GetCoord_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_interfaces::action::GetCoord_SendGoal_Response msg_;
};

class Init_GetCoord_SendGoal_Response_accepted
{
public:
  Init_GetCoord_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GetCoord_SendGoal_Response_stamp accepted(::action_interfaces::action::GetCoord_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_GetCoord_SendGoal_Response_stamp(msg_);
  }

private:
  ::action_interfaces::action::GetCoord_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_interfaces::action::GetCoord_SendGoal_Response>()
{
  return action_interfaces::action::builder::Init_GetCoord_SendGoal_Response_accepted();
}

}  // namespace action_interfaces


namespace action_interfaces
{

namespace action
{

namespace builder
{

class Init_GetCoord_GetResult_Request_goal_id
{
public:
  Init_GetCoord_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::action_interfaces::action::GetCoord_GetResult_Request goal_id(::action_interfaces::action::GetCoord_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_interfaces::action::GetCoord_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_interfaces::action::GetCoord_GetResult_Request>()
{
  return action_interfaces::action::builder::Init_GetCoord_GetResult_Request_goal_id();
}

}  // namespace action_interfaces


namespace action_interfaces
{

namespace action
{

namespace builder
{

class Init_GetCoord_GetResult_Response_result
{
public:
  explicit Init_GetCoord_GetResult_Response_result(::action_interfaces::action::GetCoord_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::action_interfaces::action::GetCoord_GetResult_Response result(::action_interfaces::action::GetCoord_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_interfaces::action::GetCoord_GetResult_Response msg_;
};

class Init_GetCoord_GetResult_Response_status
{
public:
  Init_GetCoord_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GetCoord_GetResult_Response_result status(::action_interfaces::action::GetCoord_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_GetCoord_GetResult_Response_result(msg_);
  }

private:
  ::action_interfaces::action::GetCoord_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_interfaces::action::GetCoord_GetResult_Response>()
{
  return action_interfaces::action::builder::Init_GetCoord_GetResult_Response_status();
}

}  // namespace action_interfaces


namespace action_interfaces
{

namespace action
{

namespace builder
{

class Init_GetCoord_FeedbackMessage_feedback
{
public:
  explicit Init_GetCoord_FeedbackMessage_feedback(::action_interfaces::action::GetCoord_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::action_interfaces::action::GetCoord_FeedbackMessage feedback(::action_interfaces::action::GetCoord_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_interfaces::action::GetCoord_FeedbackMessage msg_;
};

class Init_GetCoord_FeedbackMessage_goal_id
{
public:
  Init_GetCoord_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GetCoord_FeedbackMessage_feedback goal_id(::action_interfaces::action::GetCoord_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_GetCoord_FeedbackMessage_feedback(msg_);
  }

private:
  ::action_interfaces::action::GetCoord_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_interfaces::action::GetCoord_FeedbackMessage>()
{
  return action_interfaces::action::builder::Init_GetCoord_FeedbackMessage_goal_id();
}

}  // namespace action_interfaces

#endif  // ACTION_INTERFACES__ACTION__DETAIL__GET_COORD__BUILDER_HPP_
