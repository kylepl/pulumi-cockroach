// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.cockroach.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;


public final class GetClusterCertArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetClusterCertArgs Empty = new GetClusterCertArgs();

    /**
     * Cluster ID
     * 
     */
    @Import(name="id", required=true)
    private Output<String> id;

    /**
     * @return Cluster ID
     * 
     */
    public Output<String> id() {
        return this.id;
    }

    private GetClusterCertArgs() {}

    private GetClusterCertArgs(GetClusterCertArgs $) {
        this.id = $.id;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetClusterCertArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetClusterCertArgs $;

        public Builder() {
            $ = new GetClusterCertArgs();
        }

        public Builder(GetClusterCertArgs defaults) {
            $ = new GetClusterCertArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param id Cluster ID
         * 
         * @return builder
         * 
         */
        public Builder id(Output<String> id) {
            $.id = id;
            return this;
        }

        /**
         * @param id Cluster ID
         * 
         * @return builder
         * 
         */
        public Builder id(String id) {
            return id(Output.of(id));
        }

        public GetClusterCertArgs build() {
            $.id = Objects.requireNonNull($.id, "expected parameter 'id' to be non-null");
            return $;
        }
    }

}