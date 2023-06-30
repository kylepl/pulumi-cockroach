# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetPersonUserResult',
    'AwaitableGetPersonUserResult',
    'get_person_user',
    'get_person_user_output',
]

@pulumi.output_type
class GetPersonUserResult:
    """
    A collection of values returned by getPersonUser.
    """
    def __init__(__self__, email=None, id=None):
        if email and not isinstance(email, str):
            raise TypeError("Expected argument 'email' to be a str")
        pulumi.set(__self__, "email", email)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        Email address used to find the User ID.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        User ID
        """
        return pulumi.get(self, "id")


class AwaitableGetPersonUserResult(GetPersonUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPersonUserResult(
            email=self.email,
            id=self.id)


def get_person_user(email: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPersonUserResult:
    """
    Information about a person user


    :param str email: Email address used to find the User ID.
    """
    __args__ = dict()
    __args__['email'] = email
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cockroach:index/getPersonUser:getPersonUser', __args__, opts=opts, typ=GetPersonUserResult).value

    return AwaitableGetPersonUserResult(
        email=__ret__.email,
        id=__ret__.id)


@_utilities.lift_output_func(get_person_user)
def get_person_user_output(email: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPersonUserResult]:
    """
    Information about a person user


    :param str email: Email address used to find the User ID.
    """
    ...