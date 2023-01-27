# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import integer


class VpcConfiguration(AWSProperty):
    """
    `VpcConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-accesspoint-vpcconfiguration.html>`__
    """

    props: PropsDictType = {
        "VpcId": (str, False),
    }


class AccessPoint(AWSObject):
    """
    `AccessPoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html>`__
    """

    resource_type = "AWS::S3Outposts::AccessPoint"

    props: PropsDictType = {
        "Bucket": (str, True),
        "Name": (str, True),
        "Policy": (dict, False),
        "VpcConfiguration": (VpcConfiguration, True),
    }


class AbortIncompleteMultipartUpload(AWSProperty):
    """
    `AbortIncompleteMultipartUpload <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-abortincompletemultipartupload.html>`__
    """

    props: PropsDictType = {
        "DaysAfterInitiation": (integer, True),
    }


class FilterTag(AWSProperty):
    """
    `FilterTag <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-filtertag.html>`__
    """

    props: PropsDictType = {
        "Key": (str, True),
        "Value": (str, True),
    }


class FilterAndOperator(AWSProperty):
    """
    `FilterAndOperator <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-filterandoperator.html>`__
    """

    props: PropsDictType = {
        "Prefix": (str, False),
        "Tags": ([FilterTag], True),
    }


class Filter(AWSProperty):
    """
    `Filter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-filter.html>`__
    """

    props: PropsDictType = {
        "AndOperator": (FilterAndOperator, False),
        "Prefix": (str, False),
        "Tag": (FilterTag, False),
    }


class Rule(AWSProperty):
    """
    `Rule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html>`__
    """

    props: PropsDictType = {
        "AbortIncompleteMultipartUpload": (AbortIncompleteMultipartUpload, False),
        "ExpirationDate": (str, False),
        "ExpirationInDays": (integer, False),
        "Filter": (Filter, False),
        "Id": (str, False),
        "Status": (str, True),
    }


class LifecycleConfiguration(AWSProperty):
    """
    `LifecycleConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-lifecycleconfiguration.html>`__
    """

    props: PropsDictType = {
        "Rules": ([Rule], True),
    }


class Bucket(AWSObject):
    """
    `Bucket <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html>`__
    """

    resource_type = "AWS::S3Outposts::Bucket"

    props: PropsDictType = {
        "BucketName": (str, True),
        "LifecycleConfiguration": (LifecycleConfiguration, False),
        "OutpostId": (str, True),
        "Tags": (Tags, False),
    }


class BucketPolicy(AWSObject):
    """
    `BucketPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucketpolicy.html>`__
    """

    resource_type = "AWS::S3Outposts::BucketPolicy"

    props: PropsDictType = {
        "Bucket": (str, True),
        "PolicyDocument": (dict, True),
    }


class Endpoint(AWSObject):
    """
    `Endpoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html>`__
    """

    resource_type = "AWS::S3Outposts::Endpoint"

    props: PropsDictType = {
        "AccessType": (str, False),
        "CustomerOwnedIpv4Pool": (str, False),
        "OutpostId": (str, True),
        "SecurityGroupId": (str, True),
        "SubnetId": (str, True),
    }
