# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer


class ContactFlow(AWSObject):
    """
    `ContactFlow <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html>`__
    """

    resource_type = "AWS::Connect::ContactFlow"

    props: PropsDictType = {
        "Content": (str, True),
        "Description": (str, False),
        "InstanceArn": (str, True),
        "Name": (str, True),
        "State": (str, False),
        "Tags": (Tags, False),
        "Type": (str, True),
    }


class ContactFlowModule(AWSObject):
    """
    `ContactFlowModule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html>`__
    """

    resource_type = "AWS::Connect::ContactFlowModule"

    props: PropsDictType = {
        "Content": (str, True),
        "Description": (str, False),
        "InstanceArn": (str, True),
        "Name": (str, True),
        "State": (str, False),
        "Tags": (Tags, False),
    }


class HoursOfOperationTimeSlice(AWSProperty):
    """
    `HoursOfOperationTimeSlice <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationtimeslice.html>`__
    """

    props: PropsDictType = {
        "Hours": (integer, True),
        "Minutes": (integer, True),
    }


class HoursOfOperationConfig(AWSProperty):
    """
    `HoursOfOperationConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationconfig.html>`__
    """

    props: PropsDictType = {
        "Day": (str, True),
        "EndTime": (HoursOfOperationTimeSlice, True),
        "StartTime": (HoursOfOperationTimeSlice, True),
    }


class HoursOfOperation(AWSObject):
    """
    `HoursOfOperation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html>`__
    """

    resource_type = "AWS::Connect::HoursOfOperation"

    props: PropsDictType = {
        "Config": ([HoursOfOperationConfig], True),
        "Description": (str, False),
        "InstanceArn": (str, True),
        "Name": (str, True),
        "Tags": (Tags, False),
        "TimeZone": (str, True),
    }


class Attributes(AWSProperty):
    """
    `Attributes <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instance-attributes.html>`__
    """

    props: PropsDictType = {
        "AutoResolveBestVoices": (boolean, False),
        "ContactLens": (boolean, False),
        "ContactflowLogs": (boolean, False),
        "EarlyMedia": (boolean, False),
        "InboundCalls": (boolean, True),
        "OutboundCalls": (boolean, True),
        "UseCustomTTSVoices": (boolean, False),
    }


class Instance(AWSObject):
    """
    `Instance <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instance.html>`__
    """

    resource_type = "AWS::Connect::Instance"

    props: PropsDictType = {
        "Attributes": (Attributes, True),
        "DirectoryId": (str, False),
        "IdentityManagementType": (str, True),
        "InstanceAlias": (str, False),
    }


class KinesisFirehoseConfig(AWSProperty):
    """
    `KinesisFirehoseConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisfirehoseconfig.html>`__
    """

    props: PropsDictType = {
        "FirehoseArn": (str, True),
    }


class KinesisStreamConfig(AWSProperty):
    """
    `KinesisStreamConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisstreamconfig.html>`__
    """

    props: PropsDictType = {
        "StreamArn": (str, True),
    }


class EncryptionConfig(AWSProperty):
    """
    `EncryptionConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-encryptionconfig.html>`__
    """

    props: PropsDictType = {
        "EncryptionType": (str, True),
        "KeyId": (str, True),
    }


class KinesisVideoStreamConfig(AWSProperty):
    """
    `KinesisVideoStreamConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisvideostreamconfig.html>`__
    """

    props: PropsDictType = {
        "EncryptionConfig": (EncryptionConfig, False),
        "Prefix": (str, True),
        "RetentionPeriodHours": (double, True),
    }


class S3Config(AWSProperty):
    """
    `S3Config <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-s3config.html>`__
    """

    props: PropsDictType = {
        "BucketName": (str, True),
        "BucketPrefix": (str, True),
        "EncryptionConfig": (EncryptionConfig, False),
    }


class InstanceStorageConfig(AWSObject):
    """
    `InstanceStorageConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instancestorageconfig.html>`__
    """

    resource_type = "AWS::Connect::InstanceStorageConfig"

    props: PropsDictType = {
        "InstanceArn": (str, True),
        "KinesisFirehoseConfig": (KinesisFirehoseConfig, False),
        "KinesisStreamConfig": (KinesisStreamConfig, False),
        "KinesisVideoStreamConfig": (KinesisVideoStreamConfig, False),
        "ResourceType": (str, True),
        "S3Config": (S3Config, False),
        "StorageType": (str, True),
    }


class PhoneNumber(AWSObject):
    """
    `PhoneNumber <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html>`__
    """

    resource_type = "AWS::Connect::PhoneNumber"

    props: PropsDictType = {
        "CountryCode": (str, True),
        "Description": (str, False),
        "Prefix": (str, False),
        "Tags": (Tags, False),
        "TargetArn": (str, True),
        "Type": (str, True),
    }


class PhoneNumberQuickConnectConfig(AWSProperty):
    """
    `PhoneNumberQuickConnectConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-phonenumberquickconnectconfig.html>`__
    """

    props: PropsDictType = {
        "PhoneNumber": (str, True),
    }


class QueueQuickConnectConfig(AWSProperty):
    """
    `QueueQuickConnectConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-queuequickconnectconfig.html>`__
    """

    props: PropsDictType = {
        "ContactFlowArn": (str, True),
        "QueueArn": (str, True),
    }


class UserQuickConnectConfig(AWSProperty):
    """
    `UserQuickConnectConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-userquickconnectconfig.html>`__
    """

    props: PropsDictType = {
        "ContactFlowArn": (str, True),
        "UserArn": (str, True),
    }


class QuickConnectConfig(AWSProperty):
    """
    `QuickConnectConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-quickconnectconfig.html>`__
    """

    props: PropsDictType = {
        "PhoneConfig": (PhoneNumberQuickConnectConfig, False),
        "QueueConfig": (QueueQuickConnectConfig, False),
        "QuickConnectType": (str, True),
        "UserConfig": (UserQuickConnectConfig, False),
    }


class QuickConnect(AWSObject):
    """
    `QuickConnect <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html>`__
    """

    resource_type = "AWS::Connect::QuickConnect"

    props: PropsDictType = {
        "Description": (str, False),
        "InstanceArn": (str, True),
        "Name": (str, True),
        "QuickConnectConfig": (QuickConnectConfig, True),
        "Tags": (Tags, False),
    }


class EventBridgeAction(AWSProperty):
    """
    `EventBridgeAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-eventbridgeaction.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
    }


class NotificationRecipientType(AWSProperty):
    """
    `NotificationRecipientType <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-notificationrecipienttype.html>`__
    """

    props: PropsDictType = {
        "UserArns": ([str], False),
        "UserTags": (dict, False),
    }


class SendNotificationAction(AWSProperty):
    """
    `SendNotificationAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-sendnotificationaction.html>`__
    """

    props: PropsDictType = {
        "Content": (str, True),
        "ContentType": (str, True),
        "DeliveryMethod": (str, True),
        "Recipient": (NotificationRecipientType, True),
        "Subject": (str, False),
    }


class Reference(AWSProperty):
    """
    `Reference <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-reference.html>`__
    """

    props: PropsDictType = {
        "Type": (str, True),
        "Value": (str, True),
    }


class TaskAction(AWSProperty):
    """
    `TaskAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-taskaction.html>`__
    """

    props: PropsDictType = {
        "ContactFlowArn": (str, True),
        "Description": (str, False),
        "Name": (str, True),
        "References": (dict, False),
    }


class Actions(AWSProperty):
    """
    `Actions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-actions.html>`__
    """

    props: PropsDictType = {
        "AssignContactCategoryActions": (Tags, False),
        "EventBridgeActions": ([EventBridgeAction], False),
        "SendNotificationActions": ([SendNotificationAction], False),
        "TaskActions": ([TaskAction], False),
    }


class RuleTriggerEventSource(AWSProperty):
    """
    `RuleTriggerEventSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-ruletriggereventsource.html>`__
    """

    props: PropsDictType = {
        "EventSourceName": (str, True),
        "IntegrationAssociationArn": (str, False),
    }


class Rule(AWSObject):
    """
    `Rule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-rule.html>`__
    """

    resource_type = "AWS::Connect::Rule"

    props: PropsDictType = {
        "Actions": (Actions, True),
        "Function": (str, True),
        "InstanceArn": (str, True),
        "Name": (str, True),
        "PublishStatus": (str, True),
        "Tags": (Tags, False),
        "TriggerEventSource": (RuleTriggerEventSource, True),
    }


class FieldIdentifier(AWSProperty):
    """
    `FieldIdentifier <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-fieldidentifier.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
    }


class InvisibleFieldInfo(AWSProperty):
    """
    `InvisibleFieldInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-invisiblefieldinfo.html>`__
    """

    props: PropsDictType = {
        "Id": (FieldIdentifier, True),
    }


class ReadOnlyFieldInfo(AWSProperty):
    """
    `ReadOnlyFieldInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-readonlyfieldinfo.html>`__
    """

    props: PropsDictType = {
        "Id": (FieldIdentifier, True),
    }


class RequiredFieldInfo(AWSProperty):
    """
    `RequiredFieldInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-requiredfieldinfo.html>`__
    """

    props: PropsDictType = {
        "Id": (FieldIdentifier, True),
    }


class Constraints(AWSProperty):
    """
    `Constraints <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-constraints.html>`__
    """

    props: PropsDictType = {
        "InvisibleFields": ([InvisibleFieldInfo], False),
        "ReadOnlyFields": ([ReadOnlyFieldInfo], False),
        "RequiredFields": ([RequiredFieldInfo], False),
    }


class DefaultFieldValue(AWSProperty):
    """
    `DefaultFieldValue <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-defaultfieldvalue.html>`__
    """

    props: PropsDictType = {
        "DefaultValue": (str, True),
        "Id": (FieldIdentifier, True),
    }


class Field(AWSProperty):
    """
    `Field <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-field.html>`__
    """

    props: PropsDictType = {
        "Description": (str, False),
        "Id": (FieldIdentifier, True),
        "SingleSelectOptions": ([str], False),
        "Type": (str, True),
    }


class TaskTemplate(AWSObject):
    """
    `TaskTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html>`__
    """

    resource_type = "AWS::Connect::TaskTemplate"

    props: PropsDictType = {
        "ClientToken": (str, False),
        "Constraints": (Constraints, False),
        "ContactFlowArn": (str, False),
        "Defaults": ([DefaultFieldValue], False),
        "Description": (str, False),
        "Fields": ([Field], False),
        "InstanceArn": (str, True),
        "Name": (str, False),
        "Status": (str, False),
        "Tags": (Tags, False),
    }


class UserIdentityInfo(AWSProperty):
    """
    `UserIdentityInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-useridentityinfo.html>`__
    """

    props: PropsDictType = {
        "Email": (str, False),
        "FirstName": (str, False),
        "LastName": (str, False),
        "Mobile": (str, False),
        "SecondaryEmail": (str, False),
    }


class UserPhoneConfig(AWSProperty):
    """
    `UserPhoneConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-userphoneconfig.html>`__
    """

    props: PropsDictType = {
        "AfterContactWorkTimeLimit": (integer, False),
        "AutoAccept": (boolean, False),
        "DeskPhoneNumber": (str, False),
        "PhoneType": (str, True),
    }


class User(AWSObject):
    """
    `User <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html>`__
    """

    resource_type = "AWS::Connect::User"

    props: PropsDictType = {
        "DirectoryUserId": (str, False),
        "HierarchyGroupArn": (str, False),
        "IdentityInfo": (UserIdentityInfo, False),
        "InstanceArn": (str, True),
        "Password": (str, False),
        "PhoneConfig": (UserPhoneConfig, True),
        "RoutingProfileArn": (str, True),
        "SecurityProfileArns": ([str], True),
        "Tags": (Tags, False),
        "Username": (str, True),
    }


class UserHierarchyGroup(AWSObject):
    """
    `UserHierarchyGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html>`__
    """

    resource_type = "AWS::Connect::UserHierarchyGroup"

    props: PropsDictType = {
        "InstanceArn": (str, True),
        "Name": (str, True),
        "ParentGroupArn": (str, False),
    }
