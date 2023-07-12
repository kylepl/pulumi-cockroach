// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cockroach

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Metric Export Datadog Config Resource
type MetricExportDatadogConfig struct {
	pulumi.CustomResourceState

	// A Datadog API key
	ApiKey pulumi.StringOutput `pulumi:"apiKey"`
	// Cluster ID
	ClusterId pulumi.StringOutput `pulumi:"clusterId"`
	// The Datadog region to export to
	Site        pulumi.StringOutput `pulumi:"site"`
	Status      pulumi.StringOutput `pulumi:"status"`
	UserMessage pulumi.StringOutput `pulumi:"userMessage"`
}

// NewMetricExportDatadogConfig registers a new resource with the given unique name, arguments, and options.
func NewMetricExportDatadogConfig(ctx *pulumi.Context,
	name string, args *MetricExportDatadogConfigArgs, opts ...pulumi.ResourceOption) (*MetricExportDatadogConfig, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ApiKey == nil {
		return nil, errors.New("invalid value for required argument 'ApiKey'")
	}
	if args.ClusterId == nil {
		return nil, errors.New("invalid value for required argument 'ClusterId'")
	}
	if args.Site == nil {
		return nil, errors.New("invalid value for required argument 'Site'")
	}
	if args.ApiKey != nil {
		args.ApiKey = pulumi.ToSecret(args.ApiKey).(pulumi.StringInput)
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"apiKey",
	})
	opts = append(opts, secrets)
	opts = pkgResourceDefaultOpts(opts)
	var resource MetricExportDatadogConfig
	err := ctx.RegisterResource("cockroach:index/metricExportDatadogConfig:MetricExportDatadogConfig", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetMetricExportDatadogConfig gets an existing MetricExportDatadogConfig resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetMetricExportDatadogConfig(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *MetricExportDatadogConfigState, opts ...pulumi.ResourceOption) (*MetricExportDatadogConfig, error) {
	var resource MetricExportDatadogConfig
	err := ctx.ReadResource("cockroach:index/metricExportDatadogConfig:MetricExportDatadogConfig", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering MetricExportDatadogConfig resources.
type metricExportDatadogConfigState struct {
	// A Datadog API key
	ApiKey *string `pulumi:"apiKey"`
	// Cluster ID
	ClusterId *string `pulumi:"clusterId"`
	// The Datadog region to export to
	Site        *string `pulumi:"site"`
	Status      *string `pulumi:"status"`
	UserMessage *string `pulumi:"userMessage"`
}

type MetricExportDatadogConfigState struct {
	// A Datadog API key
	ApiKey pulumi.StringPtrInput
	// Cluster ID
	ClusterId pulumi.StringPtrInput
	// The Datadog region to export to
	Site        pulumi.StringPtrInput
	Status      pulumi.StringPtrInput
	UserMessage pulumi.StringPtrInput
}

func (MetricExportDatadogConfigState) ElementType() reflect.Type {
	return reflect.TypeOf((*metricExportDatadogConfigState)(nil)).Elem()
}

type metricExportDatadogConfigArgs struct {
	// A Datadog API key
	ApiKey string `pulumi:"apiKey"`
	// Cluster ID
	ClusterId string `pulumi:"clusterId"`
	// The Datadog region to export to
	Site string `pulumi:"site"`
}

// The set of arguments for constructing a MetricExportDatadogConfig resource.
type MetricExportDatadogConfigArgs struct {
	// A Datadog API key
	ApiKey pulumi.StringInput
	// Cluster ID
	ClusterId pulumi.StringInput
	// The Datadog region to export to
	Site pulumi.StringInput
}

func (MetricExportDatadogConfigArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*metricExportDatadogConfigArgs)(nil)).Elem()
}

type MetricExportDatadogConfigInput interface {
	pulumi.Input

	ToMetricExportDatadogConfigOutput() MetricExportDatadogConfigOutput
	ToMetricExportDatadogConfigOutputWithContext(ctx context.Context) MetricExportDatadogConfigOutput
}

func (*MetricExportDatadogConfig) ElementType() reflect.Type {
	return reflect.TypeOf((**MetricExportDatadogConfig)(nil)).Elem()
}

func (i *MetricExportDatadogConfig) ToMetricExportDatadogConfigOutput() MetricExportDatadogConfigOutput {
	return i.ToMetricExportDatadogConfigOutputWithContext(context.Background())
}

func (i *MetricExportDatadogConfig) ToMetricExportDatadogConfigOutputWithContext(ctx context.Context) MetricExportDatadogConfigOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MetricExportDatadogConfigOutput)
}

// MetricExportDatadogConfigArrayInput is an input type that accepts MetricExportDatadogConfigArray and MetricExportDatadogConfigArrayOutput values.
// You can construct a concrete instance of `MetricExportDatadogConfigArrayInput` via:
//
//	MetricExportDatadogConfigArray{ MetricExportDatadogConfigArgs{...} }
type MetricExportDatadogConfigArrayInput interface {
	pulumi.Input

	ToMetricExportDatadogConfigArrayOutput() MetricExportDatadogConfigArrayOutput
	ToMetricExportDatadogConfigArrayOutputWithContext(context.Context) MetricExportDatadogConfigArrayOutput
}

type MetricExportDatadogConfigArray []MetricExportDatadogConfigInput

func (MetricExportDatadogConfigArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*MetricExportDatadogConfig)(nil)).Elem()
}

func (i MetricExportDatadogConfigArray) ToMetricExportDatadogConfigArrayOutput() MetricExportDatadogConfigArrayOutput {
	return i.ToMetricExportDatadogConfigArrayOutputWithContext(context.Background())
}

func (i MetricExportDatadogConfigArray) ToMetricExportDatadogConfigArrayOutputWithContext(ctx context.Context) MetricExportDatadogConfigArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MetricExportDatadogConfigArrayOutput)
}

// MetricExportDatadogConfigMapInput is an input type that accepts MetricExportDatadogConfigMap and MetricExportDatadogConfigMapOutput values.
// You can construct a concrete instance of `MetricExportDatadogConfigMapInput` via:
//
//	MetricExportDatadogConfigMap{ "key": MetricExportDatadogConfigArgs{...} }
type MetricExportDatadogConfigMapInput interface {
	pulumi.Input

	ToMetricExportDatadogConfigMapOutput() MetricExportDatadogConfigMapOutput
	ToMetricExportDatadogConfigMapOutputWithContext(context.Context) MetricExportDatadogConfigMapOutput
}

type MetricExportDatadogConfigMap map[string]MetricExportDatadogConfigInput

func (MetricExportDatadogConfigMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*MetricExportDatadogConfig)(nil)).Elem()
}

func (i MetricExportDatadogConfigMap) ToMetricExportDatadogConfigMapOutput() MetricExportDatadogConfigMapOutput {
	return i.ToMetricExportDatadogConfigMapOutputWithContext(context.Background())
}

func (i MetricExportDatadogConfigMap) ToMetricExportDatadogConfigMapOutputWithContext(ctx context.Context) MetricExportDatadogConfigMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MetricExportDatadogConfigMapOutput)
}

type MetricExportDatadogConfigOutput struct{ *pulumi.OutputState }

func (MetricExportDatadogConfigOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**MetricExportDatadogConfig)(nil)).Elem()
}

func (o MetricExportDatadogConfigOutput) ToMetricExportDatadogConfigOutput() MetricExportDatadogConfigOutput {
	return o
}

func (o MetricExportDatadogConfigOutput) ToMetricExportDatadogConfigOutputWithContext(ctx context.Context) MetricExportDatadogConfigOutput {
	return o
}

// A Datadog API key
func (o MetricExportDatadogConfigOutput) ApiKey() pulumi.StringOutput {
	return o.ApplyT(func(v *MetricExportDatadogConfig) pulumi.StringOutput { return v.ApiKey }).(pulumi.StringOutput)
}

// Cluster ID
func (o MetricExportDatadogConfigOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v *MetricExportDatadogConfig) pulumi.StringOutput { return v.ClusterId }).(pulumi.StringOutput)
}

// The Datadog region to export to
func (o MetricExportDatadogConfigOutput) Site() pulumi.StringOutput {
	return o.ApplyT(func(v *MetricExportDatadogConfig) pulumi.StringOutput { return v.Site }).(pulumi.StringOutput)
}

func (o MetricExportDatadogConfigOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v *MetricExportDatadogConfig) pulumi.StringOutput { return v.Status }).(pulumi.StringOutput)
}

func (o MetricExportDatadogConfigOutput) UserMessage() pulumi.StringOutput {
	return o.ApplyT(func(v *MetricExportDatadogConfig) pulumi.StringOutput { return v.UserMessage }).(pulumi.StringOutput)
}

type MetricExportDatadogConfigArrayOutput struct{ *pulumi.OutputState }

func (MetricExportDatadogConfigArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*MetricExportDatadogConfig)(nil)).Elem()
}

func (o MetricExportDatadogConfigArrayOutput) ToMetricExportDatadogConfigArrayOutput() MetricExportDatadogConfigArrayOutput {
	return o
}

func (o MetricExportDatadogConfigArrayOutput) ToMetricExportDatadogConfigArrayOutputWithContext(ctx context.Context) MetricExportDatadogConfigArrayOutput {
	return o
}

func (o MetricExportDatadogConfigArrayOutput) Index(i pulumi.IntInput) MetricExportDatadogConfigOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *MetricExportDatadogConfig {
		return vs[0].([]*MetricExportDatadogConfig)[vs[1].(int)]
	}).(MetricExportDatadogConfigOutput)
}

type MetricExportDatadogConfigMapOutput struct{ *pulumi.OutputState }

func (MetricExportDatadogConfigMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*MetricExportDatadogConfig)(nil)).Elem()
}

func (o MetricExportDatadogConfigMapOutput) ToMetricExportDatadogConfigMapOutput() MetricExportDatadogConfigMapOutput {
	return o
}

func (o MetricExportDatadogConfigMapOutput) ToMetricExportDatadogConfigMapOutputWithContext(ctx context.Context) MetricExportDatadogConfigMapOutput {
	return o
}

func (o MetricExportDatadogConfigMapOutput) MapIndex(k pulumi.StringInput) MetricExportDatadogConfigOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *MetricExportDatadogConfig {
		return vs[0].(map[string]*MetricExportDatadogConfig)[vs[1].(string)]
	}).(MetricExportDatadogConfigOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*MetricExportDatadogConfigInput)(nil)).Elem(), &MetricExportDatadogConfig{})
	pulumi.RegisterInputType(reflect.TypeOf((*MetricExportDatadogConfigArrayInput)(nil)).Elem(), MetricExportDatadogConfigArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*MetricExportDatadogConfigMapInput)(nil)).Elem(), MetricExportDatadogConfigMap{})
	pulumi.RegisterOutputType(MetricExportDatadogConfigOutput{})
	pulumi.RegisterOutputType(MetricExportDatadogConfigArrayOutput{})
	pulumi.RegisterOutputType(MetricExportDatadogConfigMapOutput{})
}
