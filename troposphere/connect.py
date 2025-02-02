# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer


class ApprovedOrigin(AWSObject):
    """
    `ApprovedOrigin <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-approvedorigin.html>`__
    """

    resource_type = "AWS::Connect::ApprovedOrigin"

    props: PropsDictType = {
        "InstanceId": (str, True),
        "Origin": (str, True),
    }


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
        "Tags": (Tags, False),
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
        "EncryptionConfig": (EncryptionConfig, True),
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


class IntegrationAssociation(AWSObject):
    """
    `IntegrationAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-integrationassociation.html>`__
    """

    resource_type = "AWS::Connect::IntegrationAssociation"

    props: PropsDictType = {
        "InstanceId": (str, True),
        "IntegrationArn": (str, True),
        "IntegrationType": (str, True),
    }


class PhoneNumber(AWSObject):
    """
    `PhoneNumber <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html>`__
    """

    resource_type = "AWS::Connect::PhoneNumber"

    props: PropsDictType = {
        "CountryCode": (str, False),
        "Description": (str, False),
        "Prefix": (str, False),
        "SourcePhoneNumberArn": (str, False),
        "Tags": (Tags, False),
        "TargetArn": (str, True),
        "Type": (str, False),
    }


class Values(AWSProperty):
    """
    `Values <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-predefinedattribute-values.html>`__
    """

    props: PropsDictType = {
        "StringList": ([str], False),
    }


class PredefinedAttribute(AWSObject):
    """
    `PredefinedAttribute <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-predefinedattribute.html>`__
    """

    resource_type = "AWS::Connect::PredefinedAttribute"

    props: PropsDictType = {
        "InstanceArn": (str, True),
        "Name": (str, True),
        "Values": (Values, True),
    }


class Prompt(AWSObject):
    """
    `Prompt <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-prompt.html>`__
    """

    resource_type = "AWS::Connect::Prompt"

    props: PropsDictType = {
        "Description": (str, False),
        "InstanceArn": (str, True),
        "Name": (str, True),
        "S3Uri": (str, False),
        "Tags": (Tags, False),
    }


class OutboundCallerConfig(AWSProperty):
    """
    `OutboundCallerConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-queue-outboundcallerconfig.html>`__
    """

    props: PropsDictType = {
        "OutboundCallerIdName": (str, False),
        "OutboundCallerIdNumberArn": (str, False),
        "OutboundFlowArn": (str, False),
    }


class Queue(AWSObject):
    """
    `Queue <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-queue.html>`__
    """

    resource_type = "AWS::Connect::Queue"

    props: PropsDictType = {
        "Description": (str, False),
        "HoursOfOperationArn": (str, True),
        "InstanceArn": (str, True),
        "MaxContacts": (integer, False),
        "Name": (str, True),
        "OutboundCallerConfig": (OutboundCallerConfig, False),
        "QuickConnectArns": ([str], False),
        "Status": (str, False),
        "Tags": (Tags, False),
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


class CrossChannelBehavior(AWSProperty):
    """
    `CrossChannelBehavior <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-crosschannelbehavior.html>`__
    """

    props: PropsDictType = {
        "BehaviorType": (str, True),
    }


class MediaConcurrency(AWSProperty):
    """
    `MediaConcurrency <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-mediaconcurrency.html>`__
    """

    props: PropsDictType = {
        "Channel": (str, True),
        "Concurrency": (integer, True),
        "CrossChannelBehavior": (CrossChannelBehavior, False),
    }


class RoutingProfileQueueReference(AWSProperty):
    """
    `RoutingProfileQueueReference <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-routingprofilequeuereference.html>`__
    """

    props: PropsDictType = {
        "Channel": (str, True),
        "QueueArn": (str, True),
    }


class RoutingProfileQueueConfig(AWSProperty):
    """
    `RoutingProfileQueueConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-routingprofilequeueconfig.html>`__
    """

    props: PropsDictType = {
        "Delay": (integer, True),
        "Priority": (integer, True),
        "QueueReference": (RoutingProfileQueueReference, True),
    }


class RoutingProfile(AWSObject):
    """
    `RoutingProfile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-routingprofile.html>`__
    """

    resource_type = "AWS::Connect::RoutingProfile"

    props: PropsDictType = {
        "AgentAvailabilityTimer": (str, False),
        "DefaultOutboundQueueArn": (str, True),
        "Description": (str, True),
        "InstanceArn": (str, True),
        "MediaConcurrencies": ([MediaConcurrency], True),
        "Name": (str, True),
        "QueueConfigs": ([RoutingProfileQueueConfig], False),
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


class SecurityKey(AWSObject):
    """
    `SecurityKey <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securitykey.html>`__
    """

    resource_type = "AWS::Connect::SecurityKey"

    props: PropsDictType = {
        "InstanceId": (str, True),
        "Key": (str, True),
    }


class SecurityProfile(AWSObject):
    """
    `SecurityProfile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securityprofile.html>`__
    """

    resource_type = "AWS::Connect::SecurityProfile"

    props: PropsDictType = {
        "AllowedAccessControlTags": (Tags, False),
        "Description": (str, False),
        "InstanceArn": (str, True),
        "Permissions": ([str], False),
        "SecurityProfileName": (str, True),
        "TagRestrictedResources": ([str], False),
        "Tags": (Tags, False),
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


class TrafficDistributionGroup(AWSObject):
    """
    `TrafficDistributionGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-trafficdistributiongroup.html>`__
    """

    resource_type = "AWS::Connect::TrafficDistributionGroup"

    props: PropsDictType = {
        "Description": (str, False),
        "InstanceArn": (str, True),
        "Name": (str, True),
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


class UserProficiency(AWSProperty):
    """
    `UserProficiency <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-userproficiency.html>`__
    """

    props: PropsDictType = {
        "AttributeName": (str, True),
        "AttributeValue": (str, True),
        "Level": (double, True),
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
        "UserProficiencies": ([UserProficiency], False),
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
        "Tags": (Tags, False),
    }


class View(AWSObject):
    """
    `View <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-view.html>`__
    """

    resource_type = "AWS::Connect::View"

    props: PropsDictType = {
        "Actions": ([str], True),
        "Description": (str, False),
        "InstanceArn": (str, True),
        "Name": (str, True),
        "Tags": (Tags, False),
        "Template": (dict, True),
    }


class ViewVersion(AWSObject):
    """
    `ViewVersion <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-viewversion.html>`__
    """

    resource_type = "AWS::Connect::ViewVersion"

    props: PropsDictType = {
        "VersionDescription": (str, False),
        "ViewArn": (str, True),
        "ViewContentSha256": (str, False),
    }
