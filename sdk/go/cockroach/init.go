// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cockroach

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "cockroach:index/allowList:AllowList":
		r = &AllowList{}
	case "cockroach:index/apiOidcConfig:ApiOidcConfig":
		r = &ApiOidcConfig{}
	case "cockroach:index/caCert:CaCert":
		r = &CaCert{}
	case "cockroach:index/cluster:Cluster":
		r = &Cluster{}
	case "cockroach:index/cmek:Cmek":
		r = &Cmek{}
	case "cockroach:index/database:Database":
		r = &Database{}
	case "cockroach:index/finalizeVersionUpgrade:FinalizeVersionUpgrade":
		r = &FinalizeVersionUpgrade{}
	case "cockroach:index/folder:Folder":
		r = &Folder{}
	case "cockroach:index/logExportConfig:LogExportConfig":
		r = &LogExportConfig{}
	case "cockroach:index/maintenanceWindow:MaintenanceWindow":
		r = &MaintenanceWindow{}
	case "cockroach:index/metricExportCloudwatchConfig:MetricExportCloudwatchConfig":
		r = &MetricExportCloudwatchConfig{}
	case "cockroach:index/metricExportDatadogConfig:MetricExportDatadogConfig":
		r = &MetricExportDatadogConfig{}
	case "cockroach:index/privateEndpointConnection:PrivateEndpointConnection":
		r = &PrivateEndpointConnection{}
	case "cockroach:index/privateEndpointServices:PrivateEndpointServices":
		r = &PrivateEndpointServices{}
	case "cockroach:index/privateEndpointTrustedOwner:PrivateEndpointTrustedOwner":
		r = &PrivateEndpointTrustedOwner{}
	case "cockroach:index/sqlUser:SqlUser":
		r = &SqlUser{}
	case "cockroach:index/userRoleGrants:UserRoleGrants":
		r = &UserRoleGrants{}
	case "cockroach:index/versionDeferral:VersionDeferral":
		r = &VersionDeferral{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

type pkg struct {
	version semver.Version
}

func (p *pkg) Version() semver.Version {
	return p.version
}

func (p *pkg) ConstructProvider(ctx *pulumi.Context, name, typ, urn string) (pulumi.ProviderResource, error) {
	if typ != "pulumi:providers:cockroach" {
		return nil, fmt.Errorf("unknown provider type: %s", typ)
	}

	r := &Provider{}
	err := ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return r, err
}

func init() {
	version, _ := PkgVersion()
	pulumi.RegisterResourceModule(
		"cockroach",
		"index/allowList",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"cockroach",
		"index/apiOidcConfig",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"cockroach",
		"index/caCert",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"cockroach",
		"index/cluster",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"cockroach",
		"index/cmek",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"cockroach",
		"index/database",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"cockroach",
		"index/finalizeVersionUpgrade",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"cockroach",
		"index/folder",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"cockroach",
		"index/logExportConfig",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"cockroach",
		"index/maintenanceWindow",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"cockroach",
		"index/metricExportCloudwatchConfig",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"cockroach",
		"index/metricExportDatadogConfig",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"cockroach",
		"index/privateEndpointConnection",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"cockroach",
		"index/privateEndpointServices",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"cockroach",
		"index/privateEndpointTrustedOwner",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"cockroach",
		"index/sqlUser",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"cockroach",
		"index/userRoleGrants",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"cockroach",
		"index/versionDeferral",
		&module{version},
	)
	pulumi.RegisterResourcePackage(
		"cockroach",
		&pkg{version},
	)
}
