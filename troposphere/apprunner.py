# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer


class TraceConfiguration(AWSProperty):
    """
    `TraceConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-observabilityconfiguration-traceconfiguration.html>`__
    """

    props: PropsDictType = {
        "Vendor": (str, True),
    }


class ObservabilityConfiguration(AWSObject):
    """
    `ObservabilityConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html>`__
    """

    resource_type = "AWS::AppRunner::ObservabilityConfiguration"

    props: PropsDictType = {
        "ObservabilityConfigurationName": (str, False),
        "Tags": (Tags, False),
        "TraceConfiguration": (TraceConfiguration, False),
    }


class EncryptionConfiguration(AWSProperty):
    """
    `EncryptionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-encryptionconfiguration.html>`__
    """

    props: PropsDictType = {
        "KmsKey": (str, True),
    }


class HealthCheckConfiguration(AWSProperty):
    """
    `HealthCheckConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html>`__
    """

    props: PropsDictType = {
        "HealthyThreshold": (integer, False),
        "Interval": (integer, False),
        "Path": (str, False),
        "Protocol": (str, False),
        "Timeout": (integer, False),
        "UnhealthyThreshold": (integer, False),
    }


class InstanceConfiguration(AWSProperty):
    """
    `InstanceConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html>`__
    """

    props: PropsDictType = {
        "Cpu": (str, False),
        "InstanceRoleArn": (str, False),
        "Memory": (str, False),
    }


class EgressConfiguration(AWSProperty):
    """
    `EgressConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-egressconfiguration.html>`__
    """

    props: PropsDictType = {
        "EgressType": (str, True),
        "VpcConnectorArn": (str, False),
    }


class NetworkConfiguration(AWSProperty):
    """
    `NetworkConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-networkconfiguration.html>`__
    """

    props: PropsDictType = {
        "EgressConfiguration": (EgressConfiguration, True),
    }


class ServiceObservabilityConfiguration(AWSProperty):
    """
    `ServiceObservabilityConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-serviceobservabilityconfiguration.html>`__
    """

    props: PropsDictType = {
        "ObservabilityConfigurationArn": (str, False),
        "ObservabilityEnabled": (boolean, True),
    }


class AuthenticationConfiguration(AWSProperty):
    """
    `AuthenticationConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-authenticationconfiguration.html>`__
    """

    props: PropsDictType = {
        "AccessRoleArn": (str, False),
        "ConnectionArn": (str, False),
    }


class KeyValuePair(AWSProperty):
    """
    `KeyValuePair <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-keyvaluepair.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "Value": (str, False),
    }


class CodeConfigurationValues(AWSProperty):
    """
    `CodeConfigurationValues <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html>`__
    """

    props: PropsDictType = {
        "BuildCommand": (str, False),
        "Port": (str, False),
        "Runtime": (str, True),
        "RuntimeEnvironmentVariables": ([KeyValuePair], False),
        "StartCommand": (str, False),
    }


class CodeConfiguration(AWSProperty):
    """
    `CodeConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfiguration.html>`__
    """

    props: PropsDictType = {
        "CodeConfigurationValues": (CodeConfigurationValues, False),
        "ConfigurationSource": (str, True),
    }


class SourceCodeVersion(AWSProperty):
    """
    `SourceCodeVersion <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourcecodeversion.html>`__
    """

    props: PropsDictType = {
        "Type": (str, True),
        "Value": (str, True),
    }


class CodeRepository(AWSProperty):
    """
    `CodeRepository <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html>`__
    """

    props: PropsDictType = {
        "CodeConfiguration": (CodeConfiguration, False),
        "RepositoryUrl": (str, True),
        "SourceCodeVersion": (SourceCodeVersion, True),
    }


class ImageConfiguration(AWSProperty):
    """
    `ImageConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html>`__
    """

    props: PropsDictType = {
        "Port": (str, False),
        "RuntimeEnvironmentVariables": ([KeyValuePair], False),
        "StartCommand": (str, False),
    }


class ImageRepository(AWSProperty):
    """
    `ImageRepository <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html>`__
    """

    props: PropsDictType = {
        "ImageConfiguration": (ImageConfiguration, False),
        "ImageIdentifier": (str, True),
        "ImageRepositoryType": (str, True),
    }


class SourceConfiguration(AWSProperty):
    """
    `SourceConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html>`__
    """

    props: PropsDictType = {
        "AuthenticationConfiguration": (AuthenticationConfiguration, False),
        "AutoDeploymentsEnabled": (boolean, False),
        "CodeRepository": (CodeRepository, False),
        "ImageRepository": (ImageRepository, False),
    }


class Service(AWSObject):
    """
    `Service <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html>`__
    """

    resource_type = "AWS::AppRunner::Service"

    props: PropsDictType = {
        "AutoScalingConfigurationArn": (str, False),
        "EncryptionConfiguration": (EncryptionConfiguration, False),
        "HealthCheckConfiguration": (HealthCheckConfiguration, False),
        "InstanceConfiguration": (InstanceConfiguration, False),
        "NetworkConfiguration": (NetworkConfiguration, False),
        "ObservabilityConfiguration": (ServiceObservabilityConfiguration, False),
        "ServiceName": (str, False),
        "SourceConfiguration": (SourceConfiguration, True),
        "Tags": (Tags, False),
    }


class VpcConnector(AWSObject):
    """
    `VpcConnector <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html>`__
    """

    resource_type = "AWS::AppRunner::VpcConnector"

    props: PropsDictType = {
        "SecurityGroups": ([str], False),
        "Subnets": ([str], True),
        "Tags": (Tags, False),
        "VpcConnectorName": (str, False),
    }
