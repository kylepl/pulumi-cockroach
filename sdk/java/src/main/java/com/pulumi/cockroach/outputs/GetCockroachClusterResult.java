// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.cockroach.outputs;

import com.pulumi.cockroach.outputs.GetCockroachClusterDedicated;
import com.pulumi.cockroach.outputs.GetCockroachClusterRegion;
import com.pulumi.cockroach.outputs.GetCockroachClusterServerless;
import com.pulumi.core.annotations.CustomType;
import java.lang.String;
import java.util.List;
import java.util.Objects;

@CustomType
public final class GetCockroachClusterResult {
    private String accountId;
    private String cloudProvider;
    private String cockroachVersion;
    private String creatorId;
    private GetCockroachClusterDedicated dedicated;
    /**
     * @return The ID of this resource.
     * 
     */
    private String id;
    /**
     * @return Name of cluster
     * 
     */
    private String name;
    private String operationStatus;
    private String plan;
    private List<GetCockroachClusterRegion> regions;
    private GetCockroachClusterServerless serverless;
    private String state;
    private String upgradeStatus;

    private GetCockroachClusterResult() {}
    public String accountId() {
        return this.accountId;
    }
    public String cloudProvider() {
        return this.cloudProvider;
    }
    public String cockroachVersion() {
        return this.cockroachVersion;
    }
    public String creatorId() {
        return this.creatorId;
    }
    public GetCockroachClusterDedicated dedicated() {
        return this.dedicated;
    }
    /**
     * @return The ID of this resource.
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return Name of cluster
     * 
     */
    public String name() {
        return this.name;
    }
    public String operationStatus() {
        return this.operationStatus;
    }
    public String plan() {
        return this.plan;
    }
    public List<GetCockroachClusterRegion> regions() {
        return this.regions;
    }
    public GetCockroachClusterServerless serverless() {
        return this.serverless;
    }
    public String state() {
        return this.state;
    }
    public String upgradeStatus() {
        return this.upgradeStatus;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetCockroachClusterResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String accountId;
        private String cloudProvider;
        private String cockroachVersion;
        private String creatorId;
        private GetCockroachClusterDedicated dedicated;
        private String id;
        private String name;
        private String operationStatus;
        private String plan;
        private List<GetCockroachClusterRegion> regions;
        private GetCockroachClusterServerless serverless;
        private String state;
        private String upgradeStatus;
        public Builder() {}
        public Builder(GetCockroachClusterResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.accountId = defaults.accountId;
    	      this.cloudProvider = defaults.cloudProvider;
    	      this.cockroachVersion = defaults.cockroachVersion;
    	      this.creatorId = defaults.creatorId;
    	      this.dedicated = defaults.dedicated;
    	      this.id = defaults.id;
    	      this.name = defaults.name;
    	      this.operationStatus = defaults.operationStatus;
    	      this.plan = defaults.plan;
    	      this.regions = defaults.regions;
    	      this.serverless = defaults.serverless;
    	      this.state = defaults.state;
    	      this.upgradeStatus = defaults.upgradeStatus;
        }

        @CustomType.Setter
        public Builder accountId(String accountId) {
            this.accountId = Objects.requireNonNull(accountId);
            return this;
        }
        @CustomType.Setter
        public Builder cloudProvider(String cloudProvider) {
            this.cloudProvider = Objects.requireNonNull(cloudProvider);
            return this;
        }
        @CustomType.Setter
        public Builder cockroachVersion(String cockroachVersion) {
            this.cockroachVersion = Objects.requireNonNull(cockroachVersion);
            return this;
        }
        @CustomType.Setter
        public Builder creatorId(String creatorId) {
            this.creatorId = Objects.requireNonNull(creatorId);
            return this;
        }
        @CustomType.Setter
        public Builder dedicated(GetCockroachClusterDedicated dedicated) {
            this.dedicated = Objects.requireNonNull(dedicated);
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            this.id = Objects.requireNonNull(id);
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            this.name = Objects.requireNonNull(name);
            return this;
        }
        @CustomType.Setter
        public Builder operationStatus(String operationStatus) {
            this.operationStatus = Objects.requireNonNull(operationStatus);
            return this;
        }
        @CustomType.Setter
        public Builder plan(String plan) {
            this.plan = Objects.requireNonNull(plan);
            return this;
        }
        @CustomType.Setter
        public Builder regions(List<GetCockroachClusterRegion> regions) {
            this.regions = Objects.requireNonNull(regions);
            return this;
        }
        public Builder regions(GetCockroachClusterRegion... regions) {
            return regions(List.of(regions));
        }
        @CustomType.Setter
        public Builder serverless(GetCockroachClusterServerless serverless) {
            this.serverless = Objects.requireNonNull(serverless);
            return this;
        }
        @CustomType.Setter
        public Builder state(String state) {
            this.state = Objects.requireNonNull(state);
            return this;
        }
        @CustomType.Setter
        public Builder upgradeStatus(String upgradeStatus) {
            this.upgradeStatus = Objects.requireNonNull(upgradeStatus);
            return this;
        }
        public GetCockroachClusterResult build() {
            final var o = new GetCockroachClusterResult();
            o.accountId = accountId;
            o.cloudProvider = cloudProvider;
            o.cockroachVersion = cockroachVersion;
            o.creatorId = creatorId;
            o.dedicated = dedicated;
            o.id = id;
            o.name = name;
            o.operationStatus = operationStatus;
            o.plan = plan;
            o.regions = regions;
            o.serverless = serverless;
            o.state = state;
            o.upgradeStatus = upgradeStatus;
            return o;
        }
    }
}