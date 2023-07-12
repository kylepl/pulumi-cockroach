# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ClusterArgs', 'Cluster']

@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *,
                 cloud_provider: pulumi.Input[str],
                 name: pulumi.Input[str],
                 regions: pulumi.Input[Sequence[pulumi.Input['ClusterRegionArgs']]],
                 cockroach_version: Optional[pulumi.Input[str]] = None,
                 dedicated: Optional[pulumi.Input['ClusterDedicatedArgs']] = None,
                 serverless: Optional[pulumi.Input['ClusterServerlessArgs']] = None):
        """
        The set of arguments for constructing a Cluster resource.
        :param pulumi.Input[str] name: Name of cluster
        """
        pulumi.set(__self__, "cloud_provider", cloud_provider)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "regions", regions)
        if cockroach_version is not None:
            pulumi.set(__self__, "cockroach_version", cockroach_version)
        if dedicated is not None:
            pulumi.set(__self__, "dedicated", dedicated)
        if serverless is not None:
            pulumi.set(__self__, "serverless", serverless)

    @property
    @pulumi.getter(name="cloudProvider")
    def cloud_provider(self) -> pulumi.Input[str]:
        return pulumi.get(self, "cloud_provider")

    @cloud_provider.setter
    def cloud_provider(self, value: pulumi.Input[str]):
        pulumi.set(self, "cloud_provider", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of cluster
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def regions(self) -> pulumi.Input[Sequence[pulumi.Input['ClusterRegionArgs']]]:
        return pulumi.get(self, "regions")

    @regions.setter
    def regions(self, value: pulumi.Input[Sequence[pulumi.Input['ClusterRegionArgs']]]):
        pulumi.set(self, "regions", value)

    @property
    @pulumi.getter(name="cockroachVersion")
    def cockroach_version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cockroach_version")

    @cockroach_version.setter
    def cockroach_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cockroach_version", value)

    @property
    @pulumi.getter
    def dedicated(self) -> Optional[pulumi.Input['ClusterDedicatedArgs']]:
        return pulumi.get(self, "dedicated")

    @dedicated.setter
    def dedicated(self, value: Optional[pulumi.Input['ClusterDedicatedArgs']]):
        pulumi.set(self, "dedicated", value)

    @property
    @pulumi.getter
    def serverless(self) -> Optional[pulumi.Input['ClusterServerlessArgs']]:
        return pulumi.get(self, "serverless")

    @serverless.setter
    def serverless(self, value: Optional[pulumi.Input['ClusterServerlessArgs']]):
        pulumi.set(self, "serverless", value)


@pulumi.input_type
class _ClusterState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 cloud_provider: Optional[pulumi.Input[str]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 cockroach_version: Optional[pulumi.Input[str]] = None,
                 creator_id: Optional[pulumi.Input[str]] = None,
                 dedicated: Optional[pulumi.Input['ClusterDedicatedArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 operation_status: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input[str]] = None,
                 regions: Optional[pulumi.Input[Sequence[pulumi.Input['ClusterRegionArgs']]]] = None,
                 serverless: Optional[pulumi.Input['ClusterServerlessArgs']] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 upgrade_status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Cluster resources.
        :param pulumi.Input[str] cluster_id: The ID of this resource.
        :param pulumi.Input[str] name: Name of cluster
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if cloud_provider is not None:
            pulumi.set(__self__, "cloud_provider", cloud_provider)
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if cockroach_version is not None:
            pulumi.set(__self__, "cockroach_version", cockroach_version)
        if creator_id is not None:
            pulumi.set(__self__, "creator_id", creator_id)
        if dedicated is not None:
            pulumi.set(__self__, "dedicated", dedicated)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if operation_status is not None:
            pulumi.set(__self__, "operation_status", operation_status)
        if plan is not None:
            pulumi.set(__self__, "plan", plan)
        if regions is not None:
            pulumi.set(__self__, "regions", regions)
        if serverless is not None:
            pulumi.set(__self__, "serverless", serverless)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if upgrade_status is not None:
            pulumi.set(__self__, "upgrade_status", upgrade_status)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="cloudProvider")
    def cloud_provider(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cloud_provider")

    @cloud_provider.setter
    def cloud_provider(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cloud_provider", value)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="cockroachVersion")
    def cockroach_version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cockroach_version")

    @cockroach_version.setter
    def cockroach_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cockroach_version", value)

    @property
    @pulumi.getter(name="creatorId")
    def creator_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "creator_id")

    @creator_id.setter
    def creator_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "creator_id", value)

    @property
    @pulumi.getter
    def dedicated(self) -> Optional[pulumi.Input['ClusterDedicatedArgs']]:
        return pulumi.get(self, "dedicated")

    @dedicated.setter
    def dedicated(self, value: Optional[pulumi.Input['ClusterDedicatedArgs']]):
        pulumi.set(self, "dedicated", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of cluster
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="operationStatus")
    def operation_status(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "operation_status")

    @operation_status.setter
    def operation_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "operation_status", value)

    @property
    @pulumi.getter
    def plan(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "plan")

    @plan.setter
    def plan(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "plan", value)

    @property
    @pulumi.getter
    def regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ClusterRegionArgs']]]]:
        return pulumi.get(self, "regions")

    @regions.setter
    def regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ClusterRegionArgs']]]]):
        pulumi.set(self, "regions", value)

    @property
    @pulumi.getter
    def serverless(self) -> Optional[pulumi.Input['ClusterServerlessArgs']]:
        return pulumi.get(self, "serverless")

    @serverless.setter
    def serverless(self, value: Optional[pulumi.Input['ClusterServerlessArgs']]):
        pulumi.set(self, "serverless", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="upgradeStatus")
    def upgrade_status(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "upgrade_status")

    @upgrade_status.setter
    def upgrade_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "upgrade_status", value)


class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cloud_provider: Optional[pulumi.Input[str]] = None,
                 cockroach_version: Optional[pulumi.Input[str]] = None,
                 dedicated: Optional[pulumi.Input[pulumi.InputType['ClusterDedicatedArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 regions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ClusterRegionArgs']]]]] = None,
                 serverless: Optional[pulumi.Input[pulumi.InputType['ClusterServerlessArgs']]] = None,
                 __props__=None):
        """
        Cluster Resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Name of cluster
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Cluster Resource

        :param str resource_name: The name of the resource.
        :param ClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cloud_provider: Optional[pulumi.Input[str]] = None,
                 cockroach_version: Optional[pulumi.Input[str]] = None,
                 dedicated: Optional[pulumi.Input[pulumi.InputType['ClusterDedicatedArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 regions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ClusterRegionArgs']]]]] = None,
                 serverless: Optional[pulumi.Input[pulumi.InputType['ClusterServerlessArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClusterArgs.__new__(ClusterArgs)

            if cloud_provider is None and not opts.urn:
                raise TypeError("Missing required property 'cloud_provider'")
            __props__.__dict__["cloud_provider"] = cloud_provider
            __props__.__dict__["cockroach_version"] = cockroach_version
            __props__.__dict__["dedicated"] = dedicated
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if regions is None and not opts.urn:
                raise TypeError("Missing required property 'regions'")
            __props__.__dict__["regions"] = regions
            __props__.__dict__["serverless"] = serverless
            __props__.__dict__["account_id"] = None
            __props__.__dict__["cluster_id"] = None
            __props__.__dict__["creator_id"] = None
            __props__.__dict__["operation_status"] = None
            __props__.__dict__["plan"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["upgrade_status"] = None
        super(Cluster, __self__).__init__(
            'cockroach:index/cluster:Cluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            cloud_provider: Optional[pulumi.Input[str]] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            cockroach_version: Optional[pulumi.Input[str]] = None,
            creator_id: Optional[pulumi.Input[str]] = None,
            dedicated: Optional[pulumi.Input[pulumi.InputType['ClusterDedicatedArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            operation_status: Optional[pulumi.Input[str]] = None,
            plan: Optional[pulumi.Input[str]] = None,
            regions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ClusterRegionArgs']]]]] = None,
            serverless: Optional[pulumi.Input[pulumi.InputType['ClusterServerlessArgs']]] = None,
            state: Optional[pulumi.Input[str]] = None,
            upgrade_status: Optional[pulumi.Input[str]] = None) -> 'Cluster':
        """
        Get an existing Cluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: The ID of this resource.
        :param pulumi.Input[str] name: Name of cluster
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ClusterState.__new__(_ClusterState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["cloud_provider"] = cloud_provider
        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["cockroach_version"] = cockroach_version
        __props__.__dict__["creator_id"] = creator_id
        __props__.__dict__["dedicated"] = dedicated
        __props__.__dict__["name"] = name
        __props__.__dict__["operation_status"] = operation_status
        __props__.__dict__["plan"] = plan
        __props__.__dict__["regions"] = regions
        __props__.__dict__["serverless"] = serverless
        __props__.__dict__["state"] = state
        __props__.__dict__["upgrade_status"] = upgrade_status
        return Cluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="cloudProvider")
    def cloud_provider(self) -> pulumi.Output[str]:
        return pulumi.get(self, "cloud_provider")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="cockroachVersion")
    def cockroach_version(self) -> pulumi.Output[str]:
        return pulumi.get(self, "cockroach_version")

    @property
    @pulumi.getter(name="creatorId")
    def creator_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "creator_id")

    @property
    @pulumi.getter
    def dedicated(self) -> pulumi.Output[Optional['outputs.ClusterDedicated']]:
        return pulumi.get(self, "dedicated")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of cluster
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="operationStatus")
    def operation_status(self) -> pulumi.Output[str]:
        return pulumi.get(self, "operation_status")

    @property
    @pulumi.getter
    def plan(self) -> pulumi.Output[str]:
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter
    def regions(self) -> pulumi.Output[Sequence['outputs.ClusterRegion']]:
        return pulumi.get(self, "regions")

    @property
    @pulumi.getter
    def serverless(self) -> pulumi.Output[Optional['outputs.ClusterServerless']]:
        return pulumi.get(self, "serverless")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="upgradeStatus")
    def upgrade_status(self) -> pulumi.Output[str]:
        return pulumi.get(self, "upgrade_status")

